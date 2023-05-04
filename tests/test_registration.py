from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
class TestRegistration:
    def test_success_registration(self,driver):

      driver.get('https://stellarburgers.nomoreparties.site/register')
      driver.find_element(*TestLocators.input_name).send_keys("victoria")
      driver.find_element(*TestLocators.input_email).send_keys("victoria_test121@mail.ru")
      driver.find_element(*TestLocators.input_password).send_keys("123456")
      driver.find_element(*TestLocators.button_registration).click()
      new_url = 'https://stellarburgers.nomoreparties.site/login'
      assert 'Регистрация' in driver.find_element(*TestLocators.page_of_enter).text, "После успещной регистрации отображается название Вход"
      driver.quit()


    def test_incorrect_password(self,driver):

      driver.get('https://stellarburgers.nomoreparties.site/register')
      driver.find_element(*TestLocators.input_name).send_keys("victoria")
      driver.find_element(*TestLocators.input_email).send_keys("victoria_test119@mail.ru")
      driver.find_element(*TestLocators.input_password).send_keys("1234")
      driver.find_element(*TestLocators.button_registration).click()
      message = driver.find_element(*TestLocators.message_error)
      assert message.text == 'Некорректный пароль'
      driver.quit()


