import pytest
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from time import sleep
@pytest.fixture
def login(driver):
    login = LoginPage(driver)
    return login


@pytest.fixture
def cart(driver):
    cart = CartPage(driver)
    return cart


@pytest.mark.mark11
@pytest.mark.system
class TestCartPageNoOfProductsAddedToCart:

    def test_adding_one_product_to_cart(self,driver,home,cart):
        home.add_product1_to_cart()
        home.click_cart_button()
        assert cart.no_of_products_in_cart() == 1

    def test_adding_two_product_to_cart(self,driver,home,cart):
        home.add_product1_to_cart()
        home.add_product2_to_cart()
        home.click_cart_button()
        assert cart.no_of_products_in_cart() == 2

    def test_adding_three_product_to_cart(self,driver,home,cart):
        home.add_product1_to_cart()
        home.add_product2_to_cart()
        home.add_product3_to_cart()
        home.click_cart_button()
        assert cart.no_of_products_in_cart() == 3

    def test_adding_zero_product_to_cart(self,driver,home,base,cart):
        home.click_cart_button()
        assert base.get_text(("xpath","//*[@id='empty_cart']//b")) in "Cart is empty!"

@pytest.mark.mark12
@pytest.mark.system
class TestCartPageIsRightProductAddedToCart:
    def test_is_product1_is_added_to_cart(self,driver,home,base,cart):
        home.add_product1_to_cart()
        home.click_cart_button()
        assert base.get_text(("xpath","//*[@id='product-1']/td[2]//a")) in "Blue Top"

    def test_is_product3_is_added_to_cart(self,driver,home,base,cart):
        home.add_product3_to_cart()
        home.click_cart_button()
        assert base.get_text(("xpath","//*[@id='product-3']/td[2]//a")) in "Sleeveless Dress"
@pytest.mark.mark13
class TestCartPageAddingProductsToCartWithLogin:
    def test_add_zero_product_to_cart_with_login(self,driver,home,login,base,cart):
        home.click_signup_login_button()
        login.login_as_test_user()
        cart.click_cart_button()
        assert base.get_text(("xpath","//*[@id='empty_cart']//b")) in "Cart is empty!"
    def test_add_one_product_to_cart_with_login(self,driver,home,login,base,cart):
        try:
            home.click_signup_login_button()
            login.login_as_test_user()
            cart.click_cart_button()
            assert base.get_text(("xpath","//*[@id='empty_cart']//b")) in "Cart is empty!"
            driver.back()
            home.add_product1_to_cart()
            cart.click_cart_button()
            assert cart.no_of_products_in_cart() == 1
        finally:
            cart.delete_all_products_from_cart()

    def test_add_three_product_to_cart_with_login(self, driver, home, login, base, cart):
        try:
            home.click_signup_login_button()
            login.login_as_test_user()
            cart.click_cart_button()
            assert base.get_text(("xpath", "//*[@id='empty_cart']//b")) in "Cart is empty!"
            driver.back()
            home.add_product1_to_cart()
            home.add_product2_to_cart()
            home.add_product3_to_cart()
            cart.click_cart_button()
            assert cart.no_of_products_in_cart() == 3
        finally:
            cart.delete_all_products_from_cart()


