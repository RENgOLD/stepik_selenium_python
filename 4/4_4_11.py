from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.2/index.html')
    class_block = browser.find_elements(By.XPATH, '//*[@class="block"]')

    for i in class_block:
        button = i.find_element(By.XPATH, '//*[@class="button"]')
        button.click()

    password_text = browser.find_element(By.XPATH, '//password')
    password = password_text.text
    print(password)


