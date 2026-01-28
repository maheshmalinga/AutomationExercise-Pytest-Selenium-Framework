from pages.home_page import HomePage
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.home = HomePage(driver)
    def open_cart_page(self):
        self.home.open_home_page()
        self.home.click_cart_button()

