from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# CORRECCION: Creación del archivo urban_routes_page donde están las funciones de la página
class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    ask_taxi_button = (By.XPATH, ".//div[@class='workflow']//button[text()='Pedir un taxi']")
    comfort_button = (By.XPATH, ".//div[@class='tcard-icon']//img[@alt='Comfort']")
    phone_number_button = (By.XPATH, ".//div[@class='np-text']")
    phone_number_field = (By.XPATH, ".//input[@id='phone']")
    phone_number_next_button = (By.XPATH, ".//div[@class='modal']//button[text()='Siguiente']")
    code_sms_field = (By.XPATH, ".//input[@id='code']")
    confirm_code_button = (By.XPATH, ".//div[@class='modal']//button[text()='Confirmar']")
    payment_method_button = (By.CSS_SELECTOR, '.pp-button')
    add_card_number_button = (By.CSS_SELECTOR, '.disabled.pp-row')
    card_number_field = (By.XPATH, ".//input[@id='number']")
    card_code_field = (By.XPATH, ".//div[@class='card-code-input']/input[@id='code']")
    add_card_confirmation_button = (By.XPATH, ".//div[@class='pp-buttons']//button[text()='Agregar']")
    card_1_added = (By.ID, 'card-1')
    close_payment_method_window = (
        By.CSS_SELECTOR, '.payment-picker.open .modal .section.active .close-button.section-close')
    driver_msg_button = (By.ID, 'comment')
    handkerchief_blanket = (By.CSS_SELECTOR, '.reqs-body .r-type-switch:nth-of-type(1) .slider')
    switch_checkbox = (By.CSS_SELECTOR, 'input.switch-input')
    icecream_value = (By.CSS_SELECTOR, '.r-group-items .r-type-counter:nth-of-type(1) .counter-value')
    order_taxi_button = (By.CSS_SELECTOR, '.smart-button-main')
    order_header_title = (By.CSS_SELECTOR, '.order-header-title')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_request_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.ask_taxi_button)).click()

    def click_comfort_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.comfort_button)).click()

    def get_comfort_taxi(self):
        return self.driver.find_element(*self.comfort_button).get_property('alt')

    def click_phone_number_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.phone_number_button)).click()

    def set_phone_number(self, phone_number):
        phone_number_field = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.phone_number_field))
        phone_number_field.send_keys(phone_number)

    def click_phone_number_next_button(self):
        self.driver.find_element(*self.phone_number_next_button).click()

    def set_code_sms(self, code_sms):
        self.driver.find_element(*self.code_sms_field).send_keys(code_sms)

    def click_code_confirmation_button(self):
        self.driver.find_element(*self.confirm_code_button).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_button).text

    def click_payment_method_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.payment_method_button)).click()

    def click_add_card_number_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.add_card_number_button)).click()

    def set_card_number(self, card_number):
        card_number_field = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.card_number_field))
        card_number_field.send_keys(card_number)

    def set_card_code(self, card_code):
        card_code_field = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.card_code_field))
        card_code_field.send_keys(card_code)

    def click_add_card_confirmation_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.add_card_confirmation_button)).click()

    def send_tab(self):
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)

    def set_card(self, card_number, card_code):
        self.set_card_number(card_number)
        self.set_card_code(card_code)
        self.send_tab()
        self.click_add_card_confirmation_button()

    def get_card_id(self):
        return self.driver.find_element(*self.card_1_added)

    def is_card_1_checked(self) -> object:
        card_checkbox = self.driver.find_element(*self.card_1_added)
        return card_checkbox.is_selected()

    def click_close_payment_method_window(self):
        self.driver.find_element(*self.close_payment_method_window).click()

    def set_driver_msg(self, msg):
        driver_msg_field = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.driver_msg_button))
        driver_msg_field.send_keys(msg)
        self.send_tab()

    def get_driver_msg(self):
        return self.driver.find_element(*self.driver_msg_button).get_property('value')

    def click_handkerchief_blanket(self):
        self.driver.find_element(*self.handkerchief_blanket).click()

    def is_switch_checked(self):
        checkbox = self.driver.find_element(*self.switch_checkbox)
        return checkbox.is_selected()

    def add_icecream_amount(self, new_value):
        counter_element = self.driver.find_element(*self.icecream_value)
        self.driver.execute_script("arguments[0].textContent = arguments[1];", counter_element, new_value)

    def get_icecream_amount(self):
        return self.driver.find_element(*self.icecream_value).text

    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.order_taxi_button)).click()

    def get_driver_arrival_message(self):
        return self.driver.find_element(*self.order_header_title).text
