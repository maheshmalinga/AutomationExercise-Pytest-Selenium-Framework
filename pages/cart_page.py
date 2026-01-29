from pages.home_page import HomePage
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.home = HomePage(driver)
    #
    NO_OF_PRODUCTS = ("xpath",'//*[@class="table table-condensed"]//tbody/tr')
    CART = ("xpath", '//*[@href="/view_cart")]')

    def open_cart_page(self):
        self.home.open_home_page()
        self.home.click_cart_button()

    def no_of_products_in_cart(self):
        return len(self.find_elements(self.NO_OF_PRODUCTS))
    def click_cart_button(self):
        self.home.click_cart_button()

    def delete_product1_from_cart(self):
        products = self.find_elements(("xpath","//*[@class='cart_quantity_delete']"))
        self.click(products[0])
    def delete_product2_from_cart(self):
        products = self.find_elements(("xpath", "//*[@class='cart_quantity_delete']"))
        self.click(products[1])
    def delete_product3_from_cart(self):
        products = self.find_elements(("xpath","//*[@class='cart_quantity_delete']"))
        self.click(products[2])
    def delete_all_products_from_cart(self):
        for i in self.find_elements(("xpath","//*[@class='cart_quantity_delete']")):
            self.click(i)



