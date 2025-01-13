from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
import allure
from pages.personal_account_page import PersonalAccountPage

class OrderFeedPage(PersonalAccountPage):
    @allure.step('Получение значения всего созданных заказов')
    def get_number_creating_order(self):
        self.click_to_element(MainPageLocators.TITLE_ORDER_FEED_PAGE)
        number_order = self.get_text_from_element(OrderFeedLocators.NUMBER_OF_CREATING_ORDER)
        return number_order
