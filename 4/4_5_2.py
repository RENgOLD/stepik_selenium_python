from unittest import result

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/2/2.html')

    target_link = browser.find_element(By.LINK_TEXT, '16243162441624')
    target_link.click()

    result_text = browser.find_element(By.XPATH, '//p[@id="result"]')
    print(result_text.text)
    time.sleep(5)