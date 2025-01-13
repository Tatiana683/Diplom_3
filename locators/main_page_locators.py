from selenium.webdriver.common.by import By

class MainPageLocators:
    BUTTON_LOGIN_ACCOUNT_MAIN_PAGE = By.XPATH, ".//button[text()='Войти в аккаунт']" # Кнопка войти в форме логина
    LOGIN_INPUT_FIELD_LOGIN = By.XPATH, "//fieldset[1]//input"  # Поле ввода логина на странице авторизации
    PASSWORD_INPUT_FIELD_LOGIN = By.XPATH, "//fieldset[2]//input"  # Поле ввода пароля на странице авторизации
    BUTTON_LOGIN_PROFILE = By.XPATH, ".//button[text()='Войти']"  # Кнопка входа на странице авторизации
    BUTTON_CREATE_ORDER_MAIN_PAGE = By.XPATH, ".//button[text()='Оформить заказ']" # Кнопка на главной странице "Оформить заказ"
    BUTTON_HEADER_CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']"  # Кнопка в хеддере "Конструктор"
    BUTTON_HEADER_ORDER_FEED = By.XPATH, ".//p[text()='Лента Заказов']" # Кнопка в хеддере "Лента заказов"
    BREAD_SECTION = By.XPATH, ".//div/span[text()='Булки']"  # Таб "Булки" на странице "Конструктор"
    TITLE_ORDER_FEED_PAGE = By.XPATH, ".//h1[text()='Лента заказов']" # Заголовок страницы заказов
    ORDER_ID_NUMBER = By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]' #Номер созданного заказа в модальном окне
    TITLE_INGREDIENT_DETAILS = By.XPATH, ".//h2[text()='Детали ингредиента']" # Заголовок модалки деталей ингредиента
    CLOSE_BUTTON_MODAL_WINDOW = By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']" # Кнопка закрытия модального окна
    FLUORESCENT_BUN = By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']"  # Флюоресцентная булка в списке ингредиентов
    TARGET_CREATE_ORDER = By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']" # цель для перетягивания булки
    COUNTER_CREATING_ORDER = By.XPATH, ".//p[@class='text text_type_digits-medium mr-3']" # Каунтер стоимости заказа при оформлении
    SECTION_MODAL_WINDOW = By.XPATH, ".//div[1]/section[1]" # Локатор модального окна с деталями ингредиента
    NUMBER_IN_MODAL_WINDOW_AFTER_CREATE = By.XPATH, './/h2[@class ="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]'  # номер заказа в модально окне
    SECTION_MODAL_WINDOW_CREATING = By.XPATH, ".//section[2]"  # локатор модального окна после успешного оформления заказа
    CREATING_ORDER_MODAL_WINDOW = By.XPATH, '//*[@class="Modal_modal__P3_V5"]'  # локатор ожидания для закрытия модального окна









