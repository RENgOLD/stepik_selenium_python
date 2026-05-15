import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


with webdriver.Chrome() as browser:
    browser.get("https://stepik.org/course/104774")
    time.sleep(5)
