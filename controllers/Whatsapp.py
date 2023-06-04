from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import os
import utils.const as const
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def find_attach_input(function):
    def wrapper(self, *args, **kwargs):
        # buscamos el input de adjuntar
        adjuntar = self.driver.find_element(By.XPATH, const.ATTACH_INPUT)
        adjuntar.click()
        function(self, args[0])
        # buscamos el boton de enviar
        arrow_button = self.driver.find_element(By.XPATH, const.ARROW_BTN)
        arrow_button.click()
        time.sleep(2)
    return wrapper


class Whatsapp:
    def __init__(self) -> None:
        print("INICIANDO WHATSAPP")
        # alistamos el driver

        # PARA CHROME
        self.options = Options()
        self.options.add_argument("user-data-dir=selenium")
        self.driver = webdriver.Chrome(
            executable_path=const.PATH_CHROME_DRIVER, options=self.options)

        # abrimos whatsapp
        self.driver.get(const.WHATSAPP_URL)
        self.driver.maximize_window()
        time.sleep(10)

    def quit_driver(self) -> None:
        input("PRESIONE ENTER PARA CERRAR WHATSAPP: ")
        self.driver.quit()

    def search_contact(self, contact: str) -> None:
        print(f"BUSCANDO CONTACTO: {contact}")
        # buscamos el contacto
        search_box = self.driver.find_element(By.XPATH, const.SEARCH_INPUT)
        search_box.click()
        search_box.send_keys(contact)
        search_box.send_keys(Keys.ENTER)
        time.sleep(1)

    def send_message(self, message: str) -> None:
        print("ENVIANDO MENSAJE...")
        # bucamos el input de mensaje y mandamos el mensaje
        message_box = self.driver.find_element(By.XPATH, const.MESSAGE_INPUT)
        for i in message.split("\n"):
            message_box.send_keys(i)
            message_box.send_keys(Keys.SHIFT, Keys.ENTER)

        message_box.send_keys(Keys.ENTER)
        time.sleep(1)

    @find_attach_input
    def send_multimedia(self, image: str) -> None:
        print("ENVIANDO MULTIMEDIA...")
        ruta_imagen = os.path.abspath("temp/"+image)
        boton_imagen = self.driver.find_element(By.XPATH, const.IMAGE_INPUT)
        boton_imagen.send_keys(ruta_imagen)
        time.sleep(1)
