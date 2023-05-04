from selenium.webdriver.common.by import By
class TestLocators:
    input_name = By.XPATH,'//label[text()="Имя"]/following-sibling::input'
    input_email = By.XPATH,'//label[text()="Email"]/following-sibling::input'
    input_password = By.XPATH,'//label[text()="Пароль"]/following-sibling::input'
    button_registration = By.XPATH,'.//button[text()="Зарегистрироваться"]'
    message_error = By.XPATH, './/p[@class="input__error text_type_main-default"]'
    button_switch_on_sousi = By.XPATH, ".//span[text()='Соусы']"
    element1 = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"
    button_switch_on_nachinki = By.XPATH, ".//span[text()='Начинки']"
    element2 = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"
    button_log_in = By.LINK_TEXT, 'Личный Кабинет'
    form_fill = By.CLASS_NAME, "Auth_login__3hAey"
    button_exit = By.XPATH,'Account_button__14Yp3 text text_type_main-medium text_color_inactive'
    zagolovok_vhod = By.XPATH,'Auth_login__3hAey'
    button_sb = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a"
    zagolovok_burger = By.XPATH, "text text_type_main-large mb-5 mt-10"
    vhod_v_accaunt = By.XPATH, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"
    page_of_enter = By.XPATH, ".//div[@class='Auth_login__3hAey']/h2"
    button_input = By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'
    button_oformlenie_zakaza = By.XPATH,'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg'
    button_constructor = By.LINK_TEXT, 'Конструктор'
    istoria_zakazov = By.XPATH,'Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9'
    button_forgotten = By.XPATH,'Auth_link__1fOlj'
    page_login_registration = By.XPATH,'App_componentContainer__2JC2W'
    button_log_in_from_registration = By.XPATH,'undefined text text_type_main-default text_color_inactive mb-4'
    button_enter_on_startpage = By.XPATH, './/button[contains(text(), "Войти в аккаунт")]'


