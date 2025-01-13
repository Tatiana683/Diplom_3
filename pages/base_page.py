from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from conftest import driver
import allure
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на страницу по URL')
    def go_to_page(self, driver, url):
        self.driver.get(url)

    @allure.step('Поиск элемента с ожиданием по локатору')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу, найденному по локатору')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ввод текста в элемент, найденному по локатору')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение текста из элемента, найденного по локатору')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Получение атрибута элемента, найденному по локатору')
    def get_attribute_element(self, locator, name_attribute):
        element = self.driver.find_element(*locator)
        type_value = element.get_attribute(name_attribute)
        return type_value

    # @allure.step('Перемещение элемента по странице для Chrome')
    # def move_the_element(self, locator_element, locator_target):
    #     element = self.driver.find_element(*locator_element)
    #     target = self.driver.find_element(*locator_target)
    #     action_chains = ActionChains(self.driver)#???
    #     action_chains.drag_and_drop(element, target).perform()

    @allure.step('Перемещение элемента по странице')
    def drag_and_drop_element(self, locator_element, locator_target):
        ingredient = self.driver.find_element(*locator_element)
        basket_lst = self.driver.find_element(*locator_target)
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();
            const dragStartEvent = new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragStartEvent);

            const dragOverEvent = new DragEvent('dragover', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dragOverEvent);

            const dropEvent = new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dropEvent);

            const dragEndEvent = new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragEndEvent);
            """,
            ingredient,
            basket_lst
        )

    @allure.step('Ожидание пока текст элемента не поменяется на new_text')
    def waiting_until_text_changes(self, locator, new_text):
        WebDriverWait(self.driver, 5).until((EC.text_to_be_present_in_element(locator, new_text)))
