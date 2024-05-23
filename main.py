import data
from selenium import webdriver
from urban_routes_page import UrbanRoutesPage
from helpers import retrieve_phone_code
from helpers import wait_for_load_page
from helpers import wait_for_driver_arrival_message


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

    def setup_method(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)
        wait_for_load_page(self.driver, UrbanRoutesPage.from_field)

    # Coloca la ruta del taxi
    def test_set_route(self):
        # Llama a setup_method al inicio del test
        self.setup_method()
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    # Selecciona la opción Comfort
    def test_request_taxi_comfort(self):
        self.test_set_route()
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_button()
        taxi_type = self.routes_page.get_comfort_taxi()
        assert 'Comfort' == taxi_type

    # Agrega el número telefonico
    def test_add_phone_number(self):
        self.test_request_taxi_comfort()
        self.routes_page.click_phone_number_button()
        phone_number = data.phone_number
        self.routes_page.set_phone_number(phone_number)
        self.routes_page.click_phone_number_next_button()
        confirmation_code = retrieve_phone_code(self.driver)
        self.routes_page.set_code_sms(confirmation_code)
        self.routes_page.click_code_confirmation_button()
        phone_number_added = self.routes_page.get_phone_number()
        assert phone_number_added == phone_number

    # Agrega una tarjeta al método de pago
    def test_add_card(self):
        self.test_add_phone_number()
        self.routes_page.click_payment_method_button()
        self.routes_page.click_add_card_number_button()
        card_number, card_code = data.card_number, data.card_code
        self.routes_page.set_card(card_number, card_code)
        element = self.routes_page.card_1_added
        assert element is not None
        card_checkbox_checked = self.routes_page.is_card_1_checked()
        assert card_checkbox_checked
        self.routes_page.click_close_payment_method_window()

    # Envía un mensaje al conductor
    def test_send_driver_message(self):
        self.test_add_card()
        msg = data.message_for_driver
        self.routes_page.set_driver_msg(msg)
        driver_msg = self.routes_page.get_driver_msg()
        assert driver_msg == msg

    # Agrega pañuelos y
    def test_order_handkerchief_blanket(self):
        self.test_send_driver_message()
        self.routes_page.click_handkerchief_blanket()
        switch_checked = self.routes_page.is_switch_checked()
        assert switch_checked, "El checkbox de la clase 'switch-input' no está encendido"

    # Agrega la cantidad de helado
    def test_order_icecream(self):
        self.test_send_driver_message()
        icecream_amount = '2'
        self.routes_page.add_icecream_amount(icecream_amount)
        icecream_value = self.routes_page.get_icecream_amount()
        assert icecream_value == icecream_amount

    # Pedir el taxi ya con todos los items solicitados
    def test_order_taxi(self):
        self.test_order_icecream()
        self.routes_page.click_order_taxi_button()
        wait_for_driver_arrival_message(self.driver, UrbanRoutesPage.order_header_title)
        # Ventana que confirma que el conductor fue asignado y el tiempo que tardara en llegar
        arrival_message = self.routes_page.get_driver_arrival_message()
        assert "El conductor llegará" in arrival_message

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
