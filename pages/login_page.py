from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # --- Localizadores ---
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def _init_(self, driver):
        super()._init_(driver)

    def login(self, username, password):
        """
        Ejecuta la secuencia completa de inicio de sesión.
        """
        self.go_to_url(self.URL)

        # Escribir nombre de usuario y clave
        self._find_element(self.USERNAME_FIELD).send_keys(username)
        self._find_element(self.PASSWORD_FIELD).send_keys(password)
        self._find_element(self.USERNAME_FIELD).clear()
        self._find_element(self.PASSWORD_FIELD).clear()

        # Hacer clic en el botón de login
        self._find_element(self.LOGIN_BUTTON).click()

        def get_error_message(self) -> str:
            """
            Devuelve el texto del mensaje de error mostrado en el login.
            """
            return self._get_element_text(self.ERROR_MESSAGE)