from selenium.webdriver.common.by import By

class OrderFeedLocators:

    CREATING_ORDER_BLOCK_IN_LIST = By.XPATH, ".//li[3]/a"  # 3-й заказ в списке заказов
    NUMBER_OF_CREATING_ORDER = By.XPATH, ".//div[@class ='undefined mb-15']/p[2]" # локатор выполненных всего заказов за все время
    WORK_LIST_ORDERS = By.XPATH, './/div[1]/ul[2]' # локатор списка заказов, находящихся в работе
    LIST_ORDERS_BLOCKS = By.XPATH, './/main/div/div/ul' # локатор списка ленты заказов выполненных
    NUMBER_LAST_CREATING_ORDER_IN_LIST_ACCOUNT = By.XPATH, '//main/div/div/div/ul/li[last()]/a/div/p[1]' # локатор номера последнего созданного заказа в истории заказов




