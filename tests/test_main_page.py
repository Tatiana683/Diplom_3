from conftest import driver
from data import Constants
import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage

@allure.title('Проверка основного функционала')
class TestMainPage:
    @allure.description('В кейсе проверяется переход по клику на «Конструктор»')
    def test_go_to_constructor_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(driver, Constants.URL_LOGIN_ACCOUNT)
        main_page.click_to_element(MainPageLocators.BUTTON_HEADER_CONSTRUCTOR)
        main_page.find_element_with_wait(MainPageLocators.BREAD_SECTION)

    @allure.description('В кейсе проверяется переход по клику на «Лента заказов»')
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(driver, Constants.URL_LOGIN_ACCOUNT)
        main_page.click_to_element(MainPageLocators.BUTTON_HEADER_ORDER_FEED)
        main_page.find_element_with_wait(MainPageLocators.TITLE_ORDER_FEED_PAGE)

    @allure.description('В кейсе проверяется появление всплывающее окно с деталями, если кликнуть на ингредиент')
    def test_show_ingredients_details(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(driver, Constants.URL_MAIN_PAGE)
        main_page.click_to_element(MainPageLocators.FLUORESCENT_BUN)
        assert 'Детали ингредиента' in main_page.get_text_from_element(MainPageLocators.TITLE_INGREDIENT_DETAILS)

    @allure.description('В кейсе проверяется закрытие всплывающего окна с деталями ингредиентов для бургеров')
    def test_close_ingredients_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(driver, Constants.URL_MAIN_PAGE)
        main_page.click_to_element(MainPageLocators.FLUORESCENT_BUN)
        main_page.click_to_element(MainPageLocators.CLOSE_BUTTON_MODAL_WINDOW)
        assert 'Modal_modal__P3_V5' == main_page.get_attribute_element(MainPageLocators.SECTION_MODAL_WINDOW, 'class')

    @allure.description('В кейсе проверяется увеличивается каунтер ингредиента при добавлении в заказ')
    def test_ingredients_count_increase(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(driver, Constants.URL_MAIN_PAGE)
        # main_page.move_the_element(MainPageLocators.FLUORESCENT_BUN, MainPageLocators.TARGET_CREATE_ORDER)
        main_page.drag_and_drop_element(MainPageLocators.FLUORESCENT_BUN, MainPageLocators.TARGET_CREATE_ORDER)
        assert '1976' == main_page.get_text_from_element(MainPageLocators.COUNTER_CREATING_ORDER)

    @allure.description('В кейсе проверяется создание заказа в авторизованном аккаунте')
    def test_create_order(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(driver, Constants.URL_MAIN_PAGE)
        main_page.authorization_in_account(Constants.LOGIN_USER_2, Constants.PASSWORD_USER_2)
        main_page.find_element_with_wait(MainPageLocators.BUTTON_CREATE_ORDER_MAIN_PAGE)
        main_page.create_order(MainPageLocators.FLUORESCENT_BUN, MainPageLocators.TARGET_CREATE_ORDER)
        assert '9999'==main_page.get_text_from_element(MainPageLocators.ORDER_ID_NUMBER)
