import pytest
from pages.home_page import HomePage
from pages.base_page import BasePage

@pytest.fixture
def base(driver):
    return BasePage(driver)
@pytest.fixture
def base1(driver1):
    return BasePage(driver1)

@pytest.fixture
def home(driver):
    home = HomePage(driver)
    home.open_home_page()
    return home

@pytest.fixture(scope = "class")
def home_class(driver1):
    home = HomePage(driver1)
    home.open_home_page()
    return home

@pytest.mark.smoke
class TestHomePageHeaderElementsVisibility:

    @pytest.mark.mark4
    @pytest.mark.parametrize("element",[HomePage.HOME_BUTTON,HomePage.PRODUCTS_BUTTON,HomePage.CART_BUTTON,
                                        HomePage.SIGNUP_LOGIN_BUTTON,HomePage.TEST_CASES_BUTTON,
                                        HomePage.API_TESTING_BUTTON,HomePage.VIDEO_TUTORIALS_BUTTON,HomePage.CONTACT_US_BUTTON],
                             ids=["home button","products button","cart button","signup login button",
                                  "test cases button","api testing button","video tutorials button","contact us button"])
    def test_is_home_page_header_elements_displayed(self, home_class,base1,element):
        assert base1.is_element_clickable(element)

    # def test_is_home_button_displayed(self, home_class,base1):
    #     assert base1.is_element_clickable(home_class.HOME_BUTTON)
    # def test_is_product_button_displayed(self, home_class,base1):
    #     assert base1.is_element_clickable(home_class.PRODUCTS_BUTTON)
    # def test_is_cart_button_displayed(self, home_class,base1):
    #     assert base1.is_element_clickable(home_class.CART_BUTTON)
    # def test_is_signup_login_button_displayed(self, home_class,base1):
    #     assert base1.is_element_clickable(home_class.SIGNUP_LOGIN_BUTTON)
    # def test_is_test_cases_button_displayed(self, home_class,base1):
    #     assert base1.is_element_clickable(home_class.TEST_CASES_BUTTON)
    # def test_is_api_testing_button_displayed(self, home_class,base1):
    #     assert base1.is_element_clickable(home_class.API_TESTING_BUTTON)
    # def test_is_video_tutorials_button_displayed(self, home_class,base1):
    #     assert base1.is_element_clickable(home_class.VIDEO_TUTORIALS_BUTTON)
    # def test_is_contact_us_button_displayed(self, home_class,base1):
    #     assert base1.is_element_clickable(home_class.CONTACT_US_BUTTON)

@pytest.mark.integration
class TestHomePageHeaderElementsNavigation:

    def test_click_on_home_button(self,home):
        home.click_home_button()
        assert home.is_home_page_displayed()

    def test_click_carts_button(self,home,driver):
        home.click_cart_button()
        assert driver.current_url in "https://automationexercise.com/view_cart"
    def test_click_on_signup_login_button(self,home,driver):
        home.click_signup_login_button()
        assert driver.current_url in "https://automationexercise.com/login"
    def test_click_on_video_tutorials_button(self,home,driver):
        home.click_video_tutorials_button()
        assert driver.current_url in "https://www.youtube.com/c/AutomationExercise"

    def test_click_on_contact_us_button(self,home,driver):
        home.click_contact_us_button()
        assert driver.current_url in "https://automationexercise.com/contact_us"

    def test_click_on_test_cases_button(self,home,driver):
        home.click_test_cases_button()
        assert driver.current_url in "https://automationexercise.com/test_cases"

    def test_click_on_api_testing_button(self,home,driver):
        home.click_api_testing_button()
        assert driver.current_url in "https://automationexercise.com/api_list"
    def test_click_on_product_button(self,home,driver):
        home.click_products_button()
        assert driver.current_url in "https://automationexercise.com/products"

@pytest.mark.smoke
class TestHomePageCategoryElementVisibility:

    @pytest.mark.mark1
    @pytest.mark.parametrize("element",
                             [HomePage.WOMEN_BUTTON,HomePage.MEN_BUTTON,HomePage.KIDS_BUTTON],
                             ids=["women button","men button","kids button"])
    def test_is_category_element_displayed(self, home_class,base1,element):
        assert base1.is_element_clickable(element)

    # def test_is_women_button_displayed(self, home_class,base1):
    #     assert base1.is_element_clickable(home_class.WOMEN_BUTTON)
    # def test_is_men_button_displayed(self, home_class,base1):
    #     assert base1.is_element_clickable(home_class.MEN_BUTTON)
    # def test_is_kids_button_displayed(self, home_class,base1):
    #     assert base1.is_element_clickable(home_class.KIDS_BUTTON)
    @pytest.mark.mark2
    @pytest.mark.parametrize("element,sub_element",[(HomePage.WOMEN_BUTTON,HomePage.DRESS),
                                        (HomePage.WOMEN_BUTTON,HomePage.TOPS),
                                        (HomePage.WOMEN_BUTTON,HomePage.SAREE),
                                        (HomePage.MEN_BUTTON,HomePage.TSHIRTS),
                                        (HomePage.MEN_BUTTON,HomePage.JEANS),
                                        (HomePage.KIDS_BUTTON,HomePage.DRESS1),
                                        (HomePage.KIDS_BUTTON,HomePage.TOPS_SHIRTS)],
                             ids=["women dress","women Tops","women saree","men tshirts","men jeans","kids dress","kids tops_shirts"])
    def test_is_category_sub_element_displayed(self, home_class,base1,element,sub_element):
        base1.click(element)
        assert base1.is_element_clickable(sub_element)

    # def test_is_dress_button_displayed(self, home_class,base1):
    #     home_class.click_women_button()
    #     assert base1.is_element_clickable(home_class.DRESS)
    # def test_is_tops_button_displayed(self, home_class,base1):
    #     home_class.click_women_button()
    #     assert base1.is_element_clickable(home_class.TOPS)
    # def test_is_saree_button_displayed(self, home_class,base1):
    #     home_class.click_women_button()
    #     assert base1.is_element_clickable(home_class.SAREE)
    # def test_is_tshirts_button_displayed(self, home_class,base1):
    #     home_class.click_men_button()
    #     assert base1.is_element_clickable(home_class.TSHIRTS)
    # def test_is_jeans_button_displayed(self, home_class,base1):
    #     home_class.click_men_button()
    #     assert base1.is_element_clickable(home_class.JEANS)
    # def test_is_dress1_button_displayed(self, home_class,base1):
    #     home_class.click_kids_button()
    #     assert base1.is_element_clickable(home_class.DRESS1)
    # def test_is_tops_shirts_button_displayed(self, home_class,base1):
    #     home_class.click_kids_button()
    #     assert base1.is_element_clickable(home_class.TOPS_SHIRTS)

    ##clicking category elements

    def test_click_women_button(self,home_class,base1):
        home_class.click_women_button()
        assert base1.is_element_clickable(home_class.DRESS) and base1.is_element_clickable(home_class.TOPS) and base1.is_element_clickable(home_class.SAREE)

    def test_click_men_button(self,home_class,base1):
        home_class.click_men_button()
        assert base1.is_element_clickable(home_class.TSHIRTS) and base1.is_element_clickable(home_class.JEANS)

    def test_click_kids_button(self,home_class,base1):
        home_class.click_kids_button()
        assert base1.is_element_clickable(home_class.DRESS1) and base1.is_element_clickable(home_class.TOPS_SHIRTS)

##### test cases for category elements navigation
@pytest.mark.integration
class TestHomePageHomePageCategoryElementsNavigation:
    def test_click_dress_button(self,home,base,driver):
        home.click_dress_button()
        assert driver.current_url in "https://automationexercise.com/category_products/1"
    def test_click_tops_button(self,home,base,driver):
        home.click_tops_button()
        assert driver.current_url in "https://automationexercise.com/category_products/2"
    def test_click_saree_button(self,home,base,driver):
        home.click_saree_button()
        assert driver.current_url in "https://automationexercise.com/category_products/7"
    def test_click_tshirts_button(self,home,base,driver):
        home.click_tshirts_button()
        assert driver.current_url in "https://automationexercise.com/category_products/3"
    def test_click_jeans_button(self,home,base,driver):
        home.click_jeans_button()
        assert driver.current_url in "https://automationexercise.com/category_products/6"
    def test_click_dress1_button(self,home,base,driver):
        home.click_dress1_button()
        assert driver.current_url in "https://automationexercise.com/category_products/4"
    def test_click_tops_shirts_button(self,home,base,driver):
        home.click_tops_shirts_button()
        assert driver.current_url in "https://automationexercise.com/category_products/5"
######### test cases for the brands
@pytest.mark.smoke
class TestHomePageHomePageHomePageBrandsVisibility:
    @pytest.mark.mark3
    @pytest.mark.parametrize("element",[HomePage.POLO,HomePage.H_M,HomePage.MADAME,
                                        HomePage.MAST_HARBOUR,HomePage.BABY_HUG,HomePage.ALLEN_SOLLY_JUNIOR,
                                        HomePage.KOOKIE_KIDS,HomePage.BIBA],
                             ids=["polo button","h_m button","madame button","mast harbour button",
                                  "baby hug button","allen solly junior button","kokie kids button","biba kids button"])
    def test_is_brands_displayed(self,home_class,base1,element):
        assert base1.is_element_clickable(element)

    # def test_is_polo_button_displayed(self,home_class,base1):
    #     assert base1.is_element_clickable(home_class.POLO)
    # def test_is_h_m_button_displayed(self,home_class,base1):
    #     assert base1.is_element_clickable(home_class.H_M)
    # def test_is_madame_button_displayed(self,home_class,base1):
    #     assert base1.is_element_clickable(home_class.MADAME)
    # def test_is_mast_harbour_button_displayed(self,home_class,base1):
    #     assert base1.is_element_clickable(home_class.MAST_HARBOUR)
    # def test_is_baby_hug_button_displayed(self,home_class,base1):
    #     assert base1.is_element_clickable(home_class.BABY_HUG)
    # def test_is_allen_solly_junior_button_displayed(self,home_class,base1):
    #     assert base1.is_element_clickable(home_class.ALLEN_SOLLY_JUNIOR)
    # def test_is_kooki_kids_button_displayed(self,home_class,base1):
    #     assert base1.is_element_clickable(home_class.KOOKIE_KIDS)
    # def test_is_biba_element_displayed(self,home_class,base1):
    #     assert base1.is_element_clickable(home_class.BIBA)

@pytest.mark.integration
class TestHomePageHomePageBrandsNavigation:
    def test_click_polo_button(self,home_class,driver1):
        home_class.click_polo_button()
        assert driver1.current_url in "https://automationexercise.com/brand_products/Polo"
    def test_click_h_m_button(self,home_class,driver1):
        home_class.click_h_m_button()
        assert driver1.current_url in "https://automationexercise.com/brand_products/H&M"
    def test_click_madame_button(self,home_class,driver1):
        home_class.click_madame_button()
        assert driver1.current_url in "https://automationexercise.com/brand_products/Madame"
    def test_click_mast_harbour_button(self,home_class,driver1):
        home_class.click_mast_harbour_button()
        assert driver1.current_url in "https://automationexercise.com/brand_products/Mast%20&%20Harbour"
    def test_click_baby_hug_button(self,home_class,driver1):
        home_class.click_baby_hug_button()
        assert driver1.current_url in 'https://automationexercise.com/brand_products/Babyhug'
    def test_click_allen_solly_junior_button(self,home_class,driver1):
        home_class.click_allen_solly_junior_button()
        assert driver1.current_url in 'https://automationexercise.com/brand_products/Allen%20Solly%20Junior'
    def test_click_kooki_kids_button(self,home_class,driver1):
        home_class.click_kookie_kids_button()
        assert driver1.current_url in "https://automationexercise.com/brand_products/Kookie%20Kids"
    def test_click_biba_element_displayed(self,home_class,driver1):
        home_class.click_biba_button()
        assert driver1.current_url in "https://automationexercise.com/brand_products/Biba"



