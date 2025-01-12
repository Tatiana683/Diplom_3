import pytest
from pages.main_page import MainPage
from conftest import driver
from data import Constants
import allure

@allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')

class TestResetPasswordPage:

    @allure.description('В кейсе проверяется переход на страницу восстановления пароля')
    def test_go_to_page_reset_password(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(driver, Constants.URL_MAIN_PAGE)
        main_page.check_question_and_answer(num)
        assert main_page.get_answer_text(num) == result
