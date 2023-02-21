import os, time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# options = Options()
# options.binary_location = "/bin/google-chrome"
# driver = webdriver.Chrome(chrome_options = options, executable_path=r'/home/martindev/Documentos/chromedriver_linux64/chromedriver')


chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(options=chrome_options)


whatsapp_url = "https://web.whatsapp.com/"
driver.get(whatsapp_url)
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
search_box.send_keys("pap")
search_box.send_keys(Keys.ENTER)
message_box = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
for i in range(10):
    # time.sleep(8)
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'))).click()    
    message_box.send_keys(f"Hola {i}")
    message_box.send_keys(Keys.ENTER)
    time.sleep(8)

driver.quit()

