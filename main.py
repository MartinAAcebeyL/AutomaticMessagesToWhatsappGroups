from selenium import webdriver
import time
import os, time

from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/bin/google-chrome"
driver = webdriver.Chrome(chrome_options = options, executable_path=r'/home/martindev/Documentos/chromedriver_linux64/chromedriver')
driver.get("https://www.google.com")
time.sleep(10)
print("Chrome Browser Invoked")
driver.quit()