from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class TestCheckElements():
    def test_switch_on_element_sousi(self):##passed
     driver = webdriver.Chrome()
     driver.get('https://stellarburgers.nomoreparties.site/')
     button_switch_on_sousi = driver.find_element(By.XPATH,".//span[text()='Соусы']").click()
     element1 = driver.find_element(By.XPATH,".//p[text()='Соус Spicy-X']")
     assert element1 == driver.find_element(By.XPATH,".//p[text()='Соус Spicy-X']")
     driver.quit()

    def test_switch_on_element_nachinki(self):##passed
     driver = webdriver.Chrome()
     driver.get('https://stellarburgers.nomoreparties.site/')
     button_switch_on_nachinki = driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
     element2 = driver.find_element(By.XPATH, ".//p[text()='Сыр с астероидной плесенью']")
     assert element2 == driver.find_element(By.XPATH, ".//p[text()='Сыр с астероидной плесенью']")
     driver.quit()



