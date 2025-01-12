from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    RESSET_PASSWORD_LINK = By.XPATH, './/a[text()="Восстановить пароль"]' #Кнопка перехода на форму восстановления пароля
    RESSET_PASSWORD_BUTTON = By.XPATH, './/button[text()="Восстановить пароль"]' #Кнопка восстановления паролей
    EMAIL_INPUT_RESET_PASSWORD_PAGE = By.XPATH, '//fieldset[1]//input' #Поле ввода адреса почты в форме восстановления пароля
    SAVE_PASSWORD_BUTTON = By.XPATH, './/button[text()="Восстановить пароль"]'  # Кнопка сохранения нового пароля при восстановлении
    ICON_HIDE_PASSWORD = By.XPATH, ''#Кнопка глаза






