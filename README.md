# Proyecto de Automatizacion a Urban Routes

## Descripción del Proyecto
Este proyecto tiene como objetivo automatizar el flujo de pedir un taxi y completar los items necesarios para concluir con la orden.

## Documentación de Referencia
- **Tutorial de Python**: [Tutorial Oficial de Python](https://docs.python.org/es/3/tutorial/index.html)
- **Pytest Documentation**: Documentación completa de pytest para pruebas en Python. [Pytest](https://docs.pytest.org/en/7.1.x/contents.html)
- **PEP 8**: Guía de estilo para el código Python. [PEP](https://peps.python.org/pep-0008/)
- **Selenium WebDriver**: Guía para el uso de WebDriver de Selenium. [WebDriver](https://www.selenium.dev/documentation/webdriver/)
- **XPATH Documentation**: Guía de estilo para la sintaxis de XPATH. [XPATH](https://www.w3schools.com/xml/xpath_intro.asp)
- **CSS Documentation**: Guía de estilo para la sintaxis de CSS. [CSS Selector](https://saucelabs.com/resources/blog/selenium-tips-css-selectors)

## Tecnologías Utilizadas

### Python
Python es un lenguaje de programación de alto nivel, interpretado y con una fuerte orientación a objetos. Es ampliamente apreciado por su sintaxis clara y legible, lo que facilita tanto el aprendizaje para los nuevos programadores como el desarrollo rápido de aplicaciones complejas para los más experimentados. Python es muy popular en la automatización de tareas, el análisis de datos, la inteligencia artificial, y el desarrollo web, entre otros campos.

### PyCharm
PyCharm es un entorno de desarrollo integrado (IDE) utilizado en la programación de computadoras, específicamente para el lenguaje Python. Desarrollado por JetBrains, PyCharm ofrece varias características útiles como análisis de código, un depurador gráfico, un probador integrado, integración con sistemas de control de versiones, y soporte para el desarrollo web con Django. PyCharm facilita el desarrollo de software en Python mediante la automatización de varias tareas rutinarias y ofreciendo una interfaz cómoda para escribir, probar y depurar código.

### Selenium
Selenium es un conjunto de herramientas y bibliotecas de software utilizado principalmente para la automatización de pruebas en aplicaciones web. Uno de sus componentes es el WebDriver que proporciona una interfaz de programación para interactuar con los navegadores web de manera automatizada.

### Técnicas utilizadas:
- Automatización y control del navegador con Selenium WebDriver.
- Uso de selectores avanzados para localizar elementos usando diferentes estrategias de localización como **By.ID, By.XPATH, By.CSS_SELECTOR**.
- Sincronización de operaciones con WebDriverWait y expected_conditions.
- Estructuración de pruebas automatizadas mediante **POM**.
- Configuración y limpieza utilizando **setup_class** que establece el entorno de prueba inicial, configurando el WebDriver y **teardown_class** que asegura que el WebDriver se cierre correctamente al finalizar las pruebas.

## Comandos para Usar el Proyecto

### Clonar el Repositorio
Para obtener una copia del código fuente en tu máquina local, utiliza el siguiente comando:

```bash
git clone git@github.com:tu-usuario/qa-project-Urban-Grocers-es.git
```

Asegúrate de clonar el repositorio correcto. El nombre de usuario debe ser tu propio nombre de usuario en GIT

## Configuración en PyCharm
Para abrir el proyecto en PyCharm:

1. Abre PyCharm.
2. Selecciona Archivo → Abrir.
3. Navega hasta la carpeta qa-project-Urban-Grocers-es que clonaste y selecciona la carpeta para abrirla como un proyecto.

## Configurar WebDriver
Para utilizar el WebDriver debes de instalarlo en tu computadora, selecciona el que utilizaras para tu buscador.

[WebDriver](https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/#download-the-driver)

- Agrega la ruta a bin a la variable de entorno PATH

**Para Windows**

- Abre el Panel de Control.
- Ve a Sistema → Configuración avanzada del sistema → Variables de entorno.
- Busca y edita la variable PATH agregando la ruta completa hacia la carpeta bin que acabas de crear. Debería ser algo como C:\\WebDriver\\bin.

**Para MacOS y Linux**

- Abre la terminal.
- Ejecuta el siguiente comando para agregar la carpeta bin al PATH del sistema:

```bash
export PATH=/Users/<username>/Downloads/WebDriver/bin:$PATH
```

## Configurar Entorno de Pruebas
Para instalar Pytest y selenium, ejecuta los siguientes comandos:

```bash
pip install pytest
pip install selenium
```

## Ejecutar el Proyecto
Antes de ejecutar las pruebas, asegúrate de que el servidor está desplegado y la URL está accesible. Luego, realiza los siguientes pasos:

1. Copia la URL del servidor (sin la "/" final).
2. Establece esta URL en la variable "urban_routes_url" dentro del archivo data.py.

Para ejecutar las pruebas, usa el siguiente comando:

```bash
pytest main.py
```

Asegúrate de revisar y modificar cualquier detalle específico que pueda variar según tu configuración o requisitos del proyecto.
