from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('http://stepik.org/104774')
time.sleep(5)

browser.quit()