from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from const import *

# alistamos el driver
options = Options()
options.add_argument("user-data-dir=selenium")
options.binary_location = path_chrome_bin
driver = webdriver.Chrome(options=options, executable_path=path_chrome_driver)

# abrimos whatsapp
driver.get(whatsapp_url)
driver.maximize_window()
time.sleep(20)

# buscamos el contacto
search_box = driver.find_element(By.XPATH, search_input)
search_box.send_keys("73883448")
search_box.send_keys(Keys.ENTER)

# bucamos el input de mensaje y mandamos el mensaje
message_box = driver.find_element(By.XPATH, message_input)
message_box.send_keys(f"funciona!!!")
message_box.send_keys(Keys.ENTER)
# buscamos el input de adjuntar
adjuntar = driver.find_element(By.XPATH, attach_input)
adjuntar.click()

# buscamos el input de imagen
boton_imagen = driver.find_element(By.XPATH, image_input)
boton_imagen.send_keys(f"{path_images}/programer.jpg")

# buscamos el boton de enviar
arrow_button = driver.find_element(By.XPATH, arrow_btn)
arrow_button.click()

time.sleep(4)
driver.quit()
