from conftest import driver
from data import Constants
import allure
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from pages.personal_account_page import PersonalAccountPage

@allure.title('Проверка страницы "Личный кабинет"')
class TestMainPage:
    @allure.description('В кейсе проверяется переход по клику на «Личный кабинет»')
    def test_go_to_main_page_personal_account(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.go_to_page(driver, Constants.URL_MAIN_PAGE)
        personal_account_page.go_to_personal_account(Constants.LOGIN_USER_1, Constants.PASSWORD_USER_2)
        personal_account_page.find_element_with_wait(PersonalAccountLocators.BUTTON_HISTORY_ORDERS)

    @allure.description('В кейсе проверяется переход в раздел «История заказов»')
    def test_go_to_main_page_history_orders(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.go_to_page(driver, Constants.URL_MAIN_PAGE)
        personal_account_page.go_to_personal_account(Constants.LOGIN_USER_1, Constants.PASSWORD_USER_2)
        personal_account_page.click_to_element(PersonalAccountLocators.BUTTON_HISTORY_ORDERS)
        assert '#0165575' in personal_account_page.get_text_from_element(PersonalAccountLocators.CREATING_ORDER_BLOCK) #&&&&

    @allure.description('В кейсе проверяется выход из аккаунта')
    def test_exit_from_personal_account(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.go_to_page(driver, Constants.URL_MAIN_PAGE)
        personal_account_page.go_to_personal_account(Constants.LOGIN_USER_1, Constants.PASSWORD_USER_2)
        personal_account_page.click_to_element(PersonalAccountLocators.BUTTON_LOGOUT_PERSONAL_ACCOUNT)
        personal_account_page.find_element_with_wait(MainPageLocators.BUTTON_LOGIN_PROFILE)
