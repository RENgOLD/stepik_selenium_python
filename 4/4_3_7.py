from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
    START_BUTTON = browser.find_element(By.CSS_SELECTOR, '#showTextBtn')
    START_BUTTON.click()

    CODE_TEXT = browser.find_element(By.CSS_SELECTOR, '#text1')
    code = CODE_TEXT.text

    CODE_INPUT_FIELD = browser.find_element(By.CSS_SELECTOR, '#userInput')
    CODE_INPUT_FIELD.send_keys(code)

    SUBMIT_BUTTON = browser.find_element(By.CSS_SELECTOR, '#checkBtn')
    SUBMIT_BUTTON.click()

    ANSWER_TEXT = browser.find_element(By.CSS_SELECTOR, '#text2')
    print(ANSWER_TEXT.text)
    time.sleep(5)

