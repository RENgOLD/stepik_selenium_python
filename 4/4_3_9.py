from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
    SECRET_BUTTON = browser.find_element(By.CSS_SELECTOR, '#secret-key-button')
    SECRET_BUTTON.click()

    code = SECRET_BUTTON.get_attribute('data')
    print(code)

    time.sleep(5)

