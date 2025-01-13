import allure
from locators.personal_account_locators import PersonalAccountLocators
from pages.main_page import MainPage

class PersonalAccountPage(MainPage):
    @allure.step('Переход в личный кабинет')
    def go_to_personal_account(self, login_user, password_user):
        self.authorization_in_account(login_user, password_user)
        self.click_to_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
