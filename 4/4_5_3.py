from unittest import result

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')

    treasure_nums = browser.find_elements(By.XPATH, '//p')

    result = 0

    for num in treasure_nums:
        result += int(num.text)

    print(result)