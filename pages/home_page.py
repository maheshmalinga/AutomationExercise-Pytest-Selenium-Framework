
from pages.base_page import BasePage
from utils import config

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Header Elements Locators
    LOGO_BUTTON = ("xpath",'//*[@src="/static/images/home/logo.png"]')
    HOME_BUTTON = ("xpath",'//*[@href="/"]')
    PRODUCTS_BUTTON = ("xpath",'//*[contains(@href,"/products")]')
    CART_BUTTON = ("xpath",'//*[@href="/view_cart"]')
    SIGNUP_LOGIN_BUTTON = ("xpath",'//*[@href="/login"]')
    TEST_CASES_BUTTON = ("xpath",'//*[contains(@href,"/test_cases")]')
    API_TESTING_BUTTON = ("xpath",'//*[contains(@href,"/api_list")]')
    VIDEO_TUTORIALS_BUTTON = ("xpath",'//*[@href="https://www.youtube.com/c/AutomationExercise"]')
    CONTACT_US_BUTTON = ("xpath",'//*[@href="/contact_us"]')
    ## category elements
    WOMEN_BUTTON = ("xpath",'//*[@href="#Women"]')
    MEN_BUTTON = ("xpath",'//*[@href="#Men"]')
    KIDS_BUTTON = ("xpath",'//*[@href="#Kids"]')
    DRESS = ("xpath",'//a[@href="/category_products/1"]')
    TOPS =("xpath",'//a[@href="/category_products/2"]')
    SAREE = ("xpath",'//a[@href="/category_products/7"]')
    TSHIRTS = ("xpath",'//a[@href="/category_products/3"]')
    JEANS = ("xpath",'//a[@href="/category_products/6"]')
    DRESS1 = ("xpath",'//a[@href="/category_products/4"]')
    TOPS_SHIRTS = ("xpath",'//a[@href="/category_products/5"]')

    ## Brands
    POLO = ("xpath",'//a[@href="/brand_products/Polo"]')
    H_M = ("xpath",'//a[@href="/brand_products/H&M"]')
    MADAME = ("xpath",'//a[@href="/brand_products/Madame"]')
    MAST_HARBOUR = ("xpath",'//a[@href="/brand_products/Mast & Harbour"]')
    BABY_HUG = ("xpath",'//a[@href="/brand_products/Babyhug"]')
    ALLEN_SOLLY_JUNIOR = ("xpath",'//a[@href="/brand_products/Allen Solly Junior"]')
    KOOKIE_KIDS = ("xpath",'//a[@href="/brand_products/Kookie Kids"]')
    BIBA = ("xpath",'//a[@href="/brand_products/Biba"]')

    ##### products
    PRODUCT1 = ("xpath", '//*[@src="/get_product_picture/1"]')
    PRODUCT2 = ("xpath", '//*[@src="/get_product_picture/2"]')

    ##### cart
    CART1 = ("xpath", '//*[@data-product-id="1"]')
    CART2 = ("xpath", '//*[@data-product-id="2"]')


## methods to check visibility of header elements
    def open_home_page(self):
        self.driver.get(config.BASE_URL)

    def is_home_page_displayed(self):
        return self.driver.current_url == config.BASE_URL

    def is_logo_button_displayed(self):
        return self.is_element_clickable(self.LOGO_BUTTON)

## methods to click header elements

    def click_home_button(self):
        self.click(self.HOME_BUTTON)

    def click_products_button(self):
        self.driver.execute_script("arguments[0].click();", self.is_element_displayed(self.PRODUCTS_BUTTON))

    def click_cart_button(self):
        self.click(self.CART_BUTTON)

    def click_signup_login_button(self):
        self.click(self.SIGNUP_LOGIN_BUTTON)

    def click_test_cases_button(self):
        self.driver.execute_script("arguments[0].click();", self.is_element_displayed(self.TEST_CASES_BUTTON))

    def click_api_testing_button(self):
        self.driver.execute_script("arguments[0].click();", self.is_element_displayed(self.API_TESTING_BUTTON))

    def click_video_tutorials_button(self):
        self.click(self.VIDEO_TUTORIALS_BUTTON)

    def click_contact_us_button(self):
        self.click(self.CONTACT_US_BUTTON)

####### category elements
    def click_women_button(self):
        self.click(self.WOMEN_BUTTON)
    def click_men_button(self):
        self.click(self.MEN_BUTTON)
    def click_kids_button(self):
        self.click(self.KIDS_BUTTON)
    def click_dress_button(self):
        self.click_women_button()
        self.click(self.DRESS)
        if "google" in self.driver.current_url:
            self.driver.back()
            self.click_women_button()
            self.click(self.DRESS)
    def click_tops_button(self):
        self.click_women_button()
        element = self.is_element_displayed(self.TOPS)
        # Use JavaScript click to bypass any Ad overlays
        self.driver.execute_script("arguments[0].click();", element)
    def click_saree_button(self):
        self.click_women_button()
        element = self.is_element_displayed(self.SAREE)
        self.driver.execute_script("arguments[0].click();", element)
    def click_tshirts_button(self):
        self.click_men_button()
        element = self.is_element_displayed(self.TSHIRTS)
        self.driver.execute_script("arguments[0].click();", element)
    def click_jeans_button(self):
        self.click_men_button()
        element = self.is_element_displayed(self.JEANS)
        self.driver.execute_script("arguments[0].click();", element)
    def click_dress1_button(self):
        self.click_kids_button()
        element = self.is_element_displayed(self.DRESS1)
        self.driver.execute_script("arguments[0].click();", element)
    def click_tops_shirts_button(self):
        self.click_kids_button()
        element = self.is_element_displayed(self.TOPS_SHIRTS)
        self.driver.execute_script("arguments[0].click();", element)

########## clicking brands
    def click_polo_button(self):
        self.driver.execute_script("arguments[0].click();", self.is_element_displayed(self.POLO))
    def click_h_m_button(self):
        self.driver.execute_script("arguments[0].click();", self.is_element_displayed(self.H_M))
    def click_madame_button(self):
        self.driver.execute_script("arguments[0].click();", self.is_element_displayed(self.MADAME))
    def click_mast_harbour_button(self):
        self.driver.execute_script("arguments[0].click();", self.is_element_displayed(self.MAST_HARBOUR))
    def click_baby_hug_button(self):
        self.driver.execute_script("arguments[0].click();", self.is_element_displayed(self.BABY_HUG))
    def click_allen_solly_junior_button(self):
        self.driver.execute_script("arguments[0].click();", self.is_element_displayed(self.ALLEN_SOLLY_JUNIOR))
    def click_kookie_kids_button(self):
        self.driver.execute_script("arguments[0].click();", self.is_element_displayed(self.KOOKIE_KIDS))
    def click_biba_button(self):
        self.driver.execute_script("arguments[0].click();", self.is_element_displayed(self.BIBA))

    #### methods to check pages visibility
    # def is_products_page_displayed(self):
    #     return self.driver.current_url in "https://automationexercise.com/products"

    # def is_cart_page_displayed(self):
    #     return self.driver.current_url in "https://automationexercise.com/view_cart"

    # def is_signup_login_page_displayed(self):
    #     return self.driver.current_url in "https://automationexercise.com/login"

    # def is_test_cases_page_displayed(self):
    #     return self.driver.current_url in "https://automationexercise.com/test_cases"

    # def is_api_testing_page_displayed(self):
    #     return self.driver.current_url in "https://automationexercise.com/api_list"

    # def is_video_tutorials_page_displayed(self):
    #     return self.driver.current_url in "https://www.youtube.com/c/AutomationExercise"

    # def is_contact_us_page_displayed(self):
    #     return self.driver.current_url in "https://automationexercise.com/contact_us"

