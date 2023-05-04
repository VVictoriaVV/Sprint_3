from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
class TestCheckElements():
    def test_switch_on_element_sousi(self,driver):
     driver.find_element(*TestLocators.button_switch_on_sousi).click()
     element1 = driver.find_element(*TestLocators.element1)
     assert element1.text == 'Соусы'


    def test_switch_on_element_nachinki(self,driver):
     driver.find_element(*TestLocators.button_switch_on_nachinki).click()
     element2 = driver.find_element(*TestLocators.element2)
     assert element2.text == 'Начинки'




