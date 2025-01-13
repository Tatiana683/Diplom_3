from selenium.webdriver.common.by import By

class RecoveryPasswordLocators:
    RECOVERY_PASSWORD_LINK = By.XPATH, './/a[text()="Восстановить пароль"]' #Кнопка перехода на форму восстановления пароля
    RECOVERY_PASSWORD_BUTTON = By.XPATH, './/button[text()="Восстановить"]' #Кнопка восстановления паролей
    EMAIL_INPUT_RECOVERY_PASSWORD_PAGE = By.XPATH, '//fieldset[1]//input' #Поле ввода адреса почты в форме восстановления пароля на 1 шаге
    SAVE_PASSWORD_BUTTON = By.XPATH, './/button[text()="Сохранить"]' #Кнопка сохранения нового пароля при восстановлении
    PASSWORD_INPUT_RECOVERY_PASSWORD_PAGE = By.XPATH, '//fieldset[1]//input' #Поле ввода пароля на странице восстановления на шаге 2
    ICON_HIDE_PASSWORD = By.XPATH, './/div[@class = "input__icon input__icon-action"]'#Кнопка глаза
    INPUT_ENTER_PASSWORD = By.XPATH, './/input[@name = "Введите новый пароль"]' # поле ввода пароля






