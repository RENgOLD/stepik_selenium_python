from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')

    input_boxes = browser.find_elements(By.XPATH, '//input[@class="form"]')

    for input_box in input_boxes:
        input_box.send_keys('текст')

    send_button = browser.find_element(By.XPATH, '//input[@type="button"]')
    send_button.click()

    result_text = browser.find_element(By.XPATH, '//span[@id="result"]')
    print(result_text.text)
    time.sleep(10)



