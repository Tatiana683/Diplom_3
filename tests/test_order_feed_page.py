from conftest import driver
from data import Constants
import allure
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from locators.personal_account_locators import PersonalAccountLocators
from pages.order_feed_page import OrderFeedPage

@allure.title('Проверка страницы раздела «Лента заказов»')
class TestRecoveryPasswordPage:
    @allure.description('В кейсе проверяется открытие всплывающего окна с деталями при клике на заказ')
    def test_show_details_creating_orders(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.go_to_page(driver, Constants.URL_MAIN_PAGE)
        order_feed.click_to_element(MainPageLocators.BUTTON_HEADER_ORDER_FEED)
        order_feed.click_to_element(OrderFeedLocators.CREATING_ORDER_BLOCK_IN_LIST)
        assert "Выполнен" in order_feed.get_text_from_element(MainPageLocators.SECTION_MODAL_WINDOW_CREATING)

    @allure.description('В кейсе проверяется отображение заказа из раздела «История заказов» в разделе «Лента заказов»')
    def test_show_creating_order_in_order_feed_page(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.go_to_page(driver, Constants.URL_MAIN_PAGE)
        order_feed.go_to_personal_account(Constants.LOGIN_USER_2, Constants.PASSWORD_USER_2)
        order_feed.click_to_element(PersonalAccountLocators.BUTTON_HISTORY_ORDERS)
        number_order = order_feed.get_text_from_element(OrderFeedLocators.NUMBER_LAST_CREATING_ORDER_IN_LIST_ACCOUNT)
        order_feed.click_to_element(MainPageLocators.BUTTON_HEADER_ORDER_FEED)
        assert number_order in order_feed.get_text_from_element(OrderFeedLocators.LIST_ORDERS_BLOCKS)

    @allure.description('В кейсе проверяется увеличение счетчика «Выполнено за всё время» при создании нового заказа')
    def test_increase_counter_all_time_when_create_order(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.go_to_page(driver, Constants.URL_MAIN_PAGE)
        order_feed.authorization_in_account(Constants.LOGIN_USER_2, Constants.PASSWORD_USER_2)
        order_feed.click_to_element(MainPageLocators.BUTTON_HEADER_ORDER_FEED)
        number = order_feed.get_number_creating_order()
        order_feed.click_to_element(MainPageLocators.BUTTON_HEADER_CONSTRUCTOR)
        order_feed.create_order(MainPageLocators.FLUORESCENT_BUN, MainPageLocators.TARGET_CREATE_ORDER)
        order_feed.find_element_with_wait(MainPageLocators.CREATING_ORDER_MODAL_WINDOW)
        order_feed.click_to_element(MainPageLocators.CLOSE_BUTTON_MODAL_WINDOW)
        order_feed.click_to_element(MainPageLocators.BUTTON_HEADER_ORDER_FEED)
        new_number = order_feed.get_number_creating_order()
        assert new_number > number

    @allure.description('В кейсе проверяется появление номера заказа в разделе В работе после оформления заказа')
    def test_change_status_to_in_work(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.go_to_page(driver, Constants.URL_MAIN_PAGE)
        order_feed.authorization_in_account(Constants.LOGIN_USER_2, Constants.PASSWORD_USER_2)
        order_feed.create_order(MainPageLocators.FLUORESCENT_BUN, MainPageLocators.TARGET_CREATE_ORDER)
        order_feed.find_element_with_wait(MainPageLocators.CREATING_ORDER_MODAL_WINDOW)
        number_order = order_feed.get_text_from_element(MainPageLocators.NUMBER_IN_MODAL_WINDOW_AFTER_CREATE)
        order_feed.click_to_element(MainPageLocators.CLOSE_BUTTON_MODAL_WINDOW)
        order_feed.click_to_element(MainPageLocators.BUTTON_HEADER_ORDER_FEED)
        order_feed.waiting_until_text_changes(OrderFeedLocators.WORK_LIST_ORDERS, number_order)
        assert number_order in order_feed.get_text_from_element(OrderFeedLocators.WORK_LIST_ORDERS)
