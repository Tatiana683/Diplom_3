from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, ".//p[text()='Личный Кабинет']"  # Кнопка входа в кабинет в хеддере
    BUTTON_LOGOUT_PERSONAL_ACCOUNT = By.XPATH, ".//button[text()='Выход']"  # Кнопка выхода из профиля
    BUTTON_HISTORY_ORDERS = By.XPATH, ".//a[text()='История заказов']" # Кнопка история заказов
    CREATING_ORDER_BLOCK = By.XPATH, ".//p[text()='#0165575']" # номер в карточке созданных заказов


