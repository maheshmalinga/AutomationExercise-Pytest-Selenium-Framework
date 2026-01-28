import pytest
from pages.login_page import LoginPage
from pages.base_page import BasePage
from time import sleep

@pytest.fixture
def base1(driver1):
    return BasePage(driver1)

@pytest.fixture
def base(driver):
    return BasePage(driver)

@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    return login_page

@pytest.fixture(scope="class")
def login1(driver1):
    login1 = LoginPage(driver1)
    login1.open_login_page()
    return login1


class TestLogin:

    @pytest.mark.smoke
    def test_is_login_page_displayed(self,login):
        assert login.is_login_page_displayed()

    @pytest.mark.mark9
    @pytest.mark.unittest
    @pytest.mark.parametrize("element",
                             [LoginPage.LOGIN_EMAIL_INPUT,LoginPage.LOGIN_PASSWORD_INPUT,LoginPage.LOGIN_BUTTON,LoginPage.SIGNUP_NAME_INPUT,LoginPage.SIGNUP_EMAIL_INPUT,LoginPage.SIGNUP_BUTTON],
                             ids=["login email field","login password field","login button","signup name field","signup email field","signup button"])
    def test_is_login_page_elements_displayed(self,login1,base1,element):
        assert base1.is_element_clickable(element)

    @pytest.mark.smoke
    @pytest.mark.integration
    def test_login_with_valid_credentials(self,login):
        login.login("uishuman@gmail.com","Password@6656")
        assert login.is_logout_button_displayed()
        login.click_logout_button()

    @pytest.mark.integration
    def test_login_with_empty_credentials(self,login,driver):
        login.login("","")
        actual_message = driver.find_element(*login.LOGIN_EMAIL_INPUT).get_attribute("validationMessage")
        assert "Please fill out this field." in actual_message
    @pytest.mark.integration
    def test_login_with_no_password(self,login,driver):
        login.login("123@gmail.com","")
        actual_message = driver.find_element(*login.LOGIN_PASSWORD_INPUT).get_attribute("validationMessage")
        assert "Please fill out this field." in actual_message

    ## parametrization for the invalid credentials
    @pytest.mark.mark7
    @pytest.mark.parametrize("email,password",[("uishuman@gmail.com","123456"),("123@gmail.com","Password@6656"),("123@gmail.com","123456")],
                                 ids=["correct email wrong password","wrong email correct password","wrong email wrong password"])
    def test_login_with_invalid_credentials(self,login,email,password):
        login.login(email,password)
        assert login.get_login_error_message() in "Your email or password is incorrect!"

    # @pytest.mark.integration
    # def test_login_with_wrong_email(self, login):
    #     login.login("uishuman2@gmail.com","Password@6656")
    #     assert login.get_login_error_message() in "Your email or password is incorrect!"
    #
    # @pytest.mark.integration
    # def test_login_with_wrong_password(self, login):
    #     login.login("uishuman@gmail.com","uishuman")
    #     assert login.get_login_error_message() in "Your email or password is incorrect!"
    #
    # @pytest.mark.integration
    # def test_login_with_invalid_credentials(self, login):
    #     login.login("123@gmail.com","abcd@123")
    #     assert login.get_login_error_message() in "Your email or password is incorrect!"


@pytest.mark.mark8
class TestSignup:
    @pytest.mark.mark6
    @pytest.mark.smoke
    @pytest.mark.integration
    @pytest.mark.parametrize("name,email",[("mahesh","uisnothuman@gmail.com"),("kumar123","uishuman21@gmail.com")])
    def test_user_signup_with_not_registered_email(self,login,driver,name,email):
         login.signup(name,email)
         assert driver.current_url in "https://automationexercise.com/signup"

    @pytest.mark.integration
    @pytest.mark.smoke
    def test_user_signup_with_registered_email(self,login,driver):
        login.signup("mahesh","uishuman@gmail.com")
        assert login.get_email_already_exist_error() in "Email Address already exist!"

    @pytest.mark.integration
    def test_user_signup_with_empty_name_field(self,login,driver):
        login.signup("","")
        actual_message = driver.find_element(*login.SIGNUP_NAME_INPUT).get_attribute("validationMessage")
        assert "Please fill out this field." in actual_message
    @pytest.mark.integration
    def test_user_signup_with_empty_email_field(self,login,driver):
        login.signup("mahesh","")
        actual_message = driver.find_element(*login.LOGIN_EMAIL_INPUT).get_attribute("validationMessage")
        assert "Please fill out this field." in actual_message






