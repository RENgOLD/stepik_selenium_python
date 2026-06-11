from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.1/index.html')
    parent = browser.find_element(By.XPATH, '//*[@id="parent_id"]')

    child = parent.find_element(By.XPATH,'//*[@class="child_class"]')
    child.click()

    password = child.get_attribute('password')
    print(password)

