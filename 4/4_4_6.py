from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')
    a_tags = browser.find_elements(By.XPATH, '//a')

    result = 0
    for i, a_tag in enumerate(a_tags):
        if a_tag.get_attribute('stormtrooper').isdigit():
            result += int(a_tag.get_attribute('stormtrooper'))

    INPUT_FIELD = browser.find_element(By.XPATH, '//input[@id="inputNumber"]')
    INPUT_FIELD.send_keys(result)

    SUBMIT_BUTTON = browser.find_element(By.XPATH, '//button[@id="checkBtn"]')
    SUBMIT_BUTTON.click()

    RESULT_STRING = browser.find_element(By.XPATH, '//div[@id="feedbackMessage"]')
    print(RESULT_STRING.text)

    time.sleep(5)

