from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class TestRegistration:
    def test_success_registration(self):
      driver = webdriver.Chrome()
      driver.get('https://stellarburgers.nomoreparties.site/register')
      input_name = driver.find_element(By.XPATH,"//label[text()='Имя']/following-sibling::input").send_keys("victoria")
      input_email = driver.find_element(By.XPATH,"//label[text()='Email']/following-sibling::input").send_keys("victoria_test117@mail.ru")
      input_password = driver.find_element(By.XPATH,"//label[text()='Пароль']/following-sibling::input").send_keys("123456")
      button_registration = driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()
      WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,".//h2[text()='Вход']")))
      new_url = 'https://stellarburgers.nomoreparties.site/login'
      assert new_url == 'https://stellarburgers.nomoreparties.site/login'
      driver.quit()


    def test_incorrect_password(self):
      driver = webdriver.Chrome()
      driver.get('https://stellarburgers.nomoreparties.site/register')
      input_name = driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input").send_keys("victoria")
      input_email = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys("victoria_test114@mail.ru")
      input_password = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys("1234")
      button_registration = driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()
      message_error = driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']")
      assert message_error == driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']")
      driver.quit()


