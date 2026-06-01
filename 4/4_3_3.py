from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.1/index.html')
    START_BUTTON = browser.find_element(By.CSS_SELECTOR, 'button#clickButton')
    START_BUTTON.click()
    time.sleep(5)