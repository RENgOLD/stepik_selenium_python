from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
    DRAGON_NAME_INPUT = browser.find_element(By.CSS_SELECTOR, '#codeInput')
    DRAGON_NAME_INPUT.send_keys('Дрогон')
    SUBMIT_BUTTON = browser.find_element(By.CSS_SELECTOR, 'button#clickButton')
    SUBMIT_BUTTON.click()
    time.sleep(5)

