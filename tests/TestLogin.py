from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogIn:

    def test_log_in_click_on_button(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        button_log_in = driver.find_element(By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        but_fill_email = driver.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input').send_keys("victoria_test111@mail.ru")
        but_fill_password = driver.find_element(By.XPATH,'//label[text()="Пароль"]/following-sibling::input').send_keys("123456")
        but_lg = driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_click_on_button_an_account(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        button_log_in_new = driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        but_fill_email = driver.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input').send_keys("victoria_test111@mail.ru")
        but_fill_password = driver.find_element(By.XPATH,'//label[text()="Пароль"]/following-sibling::input').send_keys("123456")
        but_lg = driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_click_on_button_log_in_on_the_page_of_registration(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        button_log_in_from_registration = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
        but_fill_email = driver.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input').send_keys("victoria_test111@mail.ru")
        but_fill_password = driver.find_element(By.XPATH,'//label[text()="Пароль"]/following-sibling::input').send_keys("123456")
        but_lg = driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_click_on_button_forgot_password(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        button_forget_log_in = driver.find_element(By.XPATH, './/a[text()="Войти"]')
        ##WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH,".//button[text()='Восстановить']")))
        ##button_log_in_from_registration = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()
        input_email = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys("victoria_test111@mail.ru")
        but_fill_password = driver.find_element(By.CSS_SELECTOR,'#root > div > main > div > form > fieldset:nth-child(2) > div > div > input').send_keys("123456")
        but_lg = driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_change_page_on_profile(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site')
        button_log_in_account = driver.find_element(By.XPATH, '/html/body/div/div/header/nav/a/p').click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_open_constructor(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        button_log_in = driver.find_element(By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        but_fill_email = driver.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input').send_keys("victoria_test111@mail.ru")
        but_fill_password = driver.find_element(By.XPATH,'//label[text()="Пароль"]/following-sibling::input').send_keys("123456")
        but_lg = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div/main/section[2]/ul/li[1]/div")))
        driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()
        driver.find_element(By.XPATH, '/html/body/div/div/header/nav/ul/li[1]/a/p').click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

    def test_exit_from_account(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        button_log_in = driver.find_element(By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        but_fill_email = driver.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input').send_keys("victoria_test111@mail.ru")
        but_fill_password = driver.find_element(By.XPATH,'//label[text()="Пароль"]/following-sibling::input').send_keys("123456")
        but_lg = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div/main/section[2]/ul/li[1]/div")))
        driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button")))
        driver.find_element(By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button").click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div/form/button")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()