import allure
from data import Constants
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Авторизация в аккаунт')
    def authorization_in_account(self, login, password):
        self.click_to_element(MainPageLocators.BUTTON_LOGIN_ACCOUNT_MAIN_PAGE)
        self.add_text_to_element(MainPageLocators.LOGIN_INPUT_FIELD_LOGIN, login)
        self.add_text_to_element(MainPageLocators.PASSWORD_INPUT_FIELD_LOGIN, password)
        self.click_to_element(MainPageLocators.BUTTON_LOGIN_PROFILE)
        self.find_element_with_wait(MainPageLocators.BUTTON_CREATE_ORDER_MAIN_PAGE)

    @allure.step('Создание заказа')
    def create_order(self, ingredient_locator, target_locator):
        self.drag_and_drop_element(ingredient_locator, target_locator)
        self.click_to_element(MainPageLocators.BUTTON_CREATE_ORDER_MAIN_PAGE)
