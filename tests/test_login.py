from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestLogIn:

    def test_log_in_click_on_button(self,driver):

        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.button_enter_on_startpage).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.page_login_registration))
        driver.find_element(*TestLocators.input_email).send_keys("victoria_test111@mail.ru")
        driver.find_element(*TestLocators.input_password).send_keys("123456")
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.button_oformlenie_zakaza))
        assert driver.find_element(*TestLocators.button_oformlenie_zakaza) == "Оформить заказ"
        driver.quit()

    def test_click_on_button_an_account(self,driver):

        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.button_log_in).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.page_login_registration))
        driver.find_element(*TestLocators.input_email).send_keys("victoria_test111@mail.ru")
        driver.find_element(*TestLocators.input_password).send_keys("123456")
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.button_oformlenie_zakaza))
        assert driver.find_element(*TestLocators.button_oformlenie_zakaza) == "Оформить заказ"
        driver.quit()

    def test_click_on_button_log_in_on_the_page_of_registration(self,driver):

        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*TestLocators.button_log_in_from_registration).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.page_login_registration))
        driver.find_element(*TestLocators.input_email).send_keys("victoria_test111@mail.ru")
        driver.find_element(*TestLocators.input_password).send_keys("123456")
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.button_oformlenie_zakaza))
        assert driver.find_element(*TestLocators.button_oformlenie_zakaza) == "Оформить заказ"
        driver.quit()

    def test_click_on_button_forgot_password(self,driver):

        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*TestLocators.button_input)
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(*TestLocators.button_forgotten))
        driver.find_element().click(*TestLocators.button_forgotten)
        driver.find_element(*TestLocators.input_email).send_keys("victoria_test111@mail.ru")
        driver.find_element(*TestLocators.input_password).send_keys("123456")
        driver.find_element(*TestLocators.button_input).click()
        assert driver.find_element(*TestLocators.button_oformlenie_zakaza) == "Оформить заказ"
        driver.quit()

    def test_change_page_on_profile(self,driver):

        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.vhod_v_accaunt).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.page_of_enter))
        driver.find_element(*TestLocators.input_email).send_keys("victoria_test111@mail.ru")
        driver.find_element(*TestLocators.input_password).send_keys("123456")
        driver.find_element(*TestLocators.button_input).click()
        istoria = driver.find_element(*TestLocators.button_personal_account).click()
        assert istoria.text == "История заказов"
        driver.quit()

    def test_open_constructor(self,driver):

        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.vhod_v_accaunt).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.page_of_enter))
        driver.find_element(*TestLocators.input_email).send_keys("victoria_test111@mail.ru")
        driver.find_element(*TestLocators.input_password).send_keys("123456")
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(*TestLocators.button_constructor))
        driver.find_element(*TestLocators.button_constructor).click()
        assert driver.find_element(*TestLocators.button_oformlenie_zakaza) == "Оформить заказ"
        driver.quit()

    def test_click_Stellar_Burgers(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(*TestLocators.form_for_filling))
        driver.find_element(*TestLocators.input_email).send_keys("victoria_test111@mail.ru")
        driver.find_element(*TestLocators.input_password).send_keys('123456')
        driver.find_element(*TestLocators.button_registration).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(*TestLocators.button_log_in))
        driver.find_element(*TestLocators.button_log_in).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*TestLocators.button_exit))
        driver.find_element(*TestLocators.button_sb).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(*TestLocators.zagolovok_burger))
        burger = driver.find_element(*TestLocators.zagolovok_burger)
        assert burger.text == 'Соберите бургер'

    def test_exit_from_account(self,driver):
        driver.find_element(*TestLocators.button_log_in).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*TestLocators.form_fill))
        driver.find_element(*TestLocators.input_email).send_keys("victoria_test111@mail.ru")
        driver.find_element(*TestLocators.input_password).send_keys("123456")
        driver.find_element(*TestLocators.button_registration).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(*TestLocators.button_log_in))
        driver.find_element(*TestLocators.button_log_in).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(*TestLocators.button_exit))
        driver.find_element(*TestLocators.button_exit).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(*TestLocators.zagolovok_vhod))
        assert driver.find_element(*TestLocators.zagolovok_vhod).text == "Вход"
        driver.quit()
