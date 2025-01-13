from conftest import driver
from data import Constants
import allure
from locators.recovery_password_locators import RecoveryPasswordLocators
from pages.main_page import MainPage

@allure.title('Проверка страницы "Восстановление пароля"')
class TestResetPasswordPage:

    @allure.description('В кейсе проверяется переход на страницу восстановления пароля')
    def test_go_to_page_recovery_password(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(driver, Constants.URL_LOGIN_ACCOUNT)
        main_page.click_to_element(RecoveryPasswordLocators.RECOVERY_PASSWORD_LINK)
        assert "Восстановить" in main_page.get_text_from_element(RecoveryPasswordLocators.RECOVERY_PASSWORD_BUTTON)

    @allure.description('В кейсе проверяется ввод почты и клик по кнопке «Восстановить»')
    def test_click_on_the_restore_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(driver, Constants.URL_LOGIN_ACCOUNT)
        main_page.click_to_element(RecoveryPasswordLocators.RECOVERY_PASSWORD_LINK)
        main_page.add_text_to_element(RecoveryPasswordLocators.EMAIL_INPUT_RECOVERY_PASSWORD_PAGE, Constants.LOGIN_USER_1)
        main_page.click_to_element(RecoveryPasswordLocators.RECOVERY_PASSWORD_BUTTON)
        assert "Сохранить" in main_page.get_text_from_element(RecoveryPasswordLocators.SAVE_PASSWORD_BUTTON)

    @allure.description('В кейсе проверяется, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_password_in_field(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(driver, Constants.URL_LOGIN_ACCOUNT)
        main_page.click_to_element(RecoveryPasswordLocators.RECOVERY_PASSWORD_LINK)
        main_page.add_text_to_element(RecoveryPasswordLocators.EMAIL_INPUT_RECOVERY_PASSWORD_PAGE, Constants.LOGIN_USER_1)
        main_page.click_to_element(RecoveryPasswordLocators.RECOVERY_PASSWORD_BUTTON)
        main_page.find_element_with_wait(RecoveryPasswordLocators.SAVE_PASSWORD_BUTTON)
        main_page.add_text_to_element(RecoveryPasswordLocators.PASSWORD_INPUT_RECOVERY_PASSWORD_PAGE, Constants.PASSWORD_USER_1)
        main_page.click_to_element(RecoveryPasswordLocators.ICON_HIDE_PASSWORD)
        assert 'text' == main_page.get_attribute_element(RecoveryPasswordLocators.INPUT_ENTER_PASSWORD, 'type')
