from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("user-data-dir=selenium")
options.binary_location = "/bin/google-chrome"
driver = webdriver.Chrome(
    options=options, executable_path=r'/home/martindev/Documentos/chromedriver_linux64/chromedriver')


whatsapp_url = "https://web.whatsapp.com/"
driver.get(whatsapp_url)
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(20)

search_box = driver.find_element(
    By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
search_box.send_keys("73883448")
search_box.send_keys(Keys.ENTER)

path_message_box = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'

#
message_box = driver.find_element(By.XPATH, path_message_box)

message_box.send_keys(f"funciona!!!")
message_box.send_keys(Keys.ENTER)

adjuntar = driver.find_element(
    By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'
)
adjuntar.click()

boton_imagen = driver.find_element(By.XPATH,
                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input')

boton_imagen.send_keys("/home/martindev/Descargas/programer.jpg")

arrow_button = driver.find_element(
    By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div')
arrow_button.click()

time.sleep(4)

driver.quit()
