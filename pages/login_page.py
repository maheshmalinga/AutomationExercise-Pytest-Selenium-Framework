from pages.base_page import BasePage
from pages.home_page import HomePage

class LoginPage(BasePage):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)
        self.home_page = HomePage(driver)

    def open_login_page(self):
        self.home_page.open_home_page()
        self.home_page.click_signup_login_button()

    def is_login_page_displayed(self):
        return self.driver.current_url in "https://automationexercise.com/login"

    ## LOGIN
    LOGIN_EMAIL_INPUT = ("xpath",'//*[@data-qa="login-emaill"]')
    LOGIN_PASSWORD_INPUT = ("xpath",'//*[@data-qa="login-password"]')
    LOGIN_BUTTON = ("xpath",'//*[@data-qa="login-button"]')
    INCORRECT_EMAIL_PASSWORD_ERROR = ("xpath",'//*[@data-qa="login-password"]/..//p')
    ## SIGNUP
    SIGNUP_NAME_INPUT = ("xpath",'//*[@data-qa="signup-name"]')
    SIGNUP_EMAIL_INPUT = ("xpath",'//*[@data-qa="signup-email"]')
    SIGNUP_BUTTON = ("xpath",'//*[@data-qa="signup-button"]')
    EMAIL_ALREADY_EXIST_ERROR = ("xpath",'//*[@data-qa="signup-email"]/..//p')
    LOG_OUT_BUTTON = ("xpath",'//*[@href="/logout"]')

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)
    def get_login_error_message(self):
        return self.get_text(self.INCORRECT_EMAIL_PASSWORD_ERROR)
    def click_signup_button(self):
        self.click(self.SIGNUP_BUTTON)
    def is_logout_button_displayed(self):
        return self.is_element_clickable(self.LOG_OUT_BUTTON)
    def click_logout_button(self):
        self.click(self.LOG_OUT_BUTTON)
    def get_email_already_exist_error(self):
        return self.get_text(self.EMAIL_ALREADY_EXIST_ERROR)

    def login(self, email, password):
        self.enter_text(self.LOGIN_EMAIL_INPUT,email)
        self.enter_text(self.LOGIN_PASSWORD_INPUT,password)
        self.click_login_button()

    def signup(self, name,email):
        self.enter_text(self.SIGNUP_NAME_INPUT,name)
        self.enter_text(self.SIGNUP_EMAIL_INPUT,email)
        self.click_signup_button()



