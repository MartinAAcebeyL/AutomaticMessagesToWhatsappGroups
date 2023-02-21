

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(options=chrome_options)

# Abre WhatsApp Web
driver.get("https://web.whatsapp.com/")
# input("Presiona ENTER después de escanear el código QR")

# Guarda la sesión
driver.quit()