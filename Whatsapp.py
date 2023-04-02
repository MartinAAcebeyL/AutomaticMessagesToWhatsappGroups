from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import const


def find_attach_input(function: function):
    def wrapper(self):
        # buscamos el input de adjuntar
        adjuntar = self.driver.find_element(By.XPATH, const.attach_input)
        adjuntar.click()
        function(self)
        # buscamos el boton de enviar
        arrow_button = self.driver.find_element(By.XPATH, const.arrow_btn)
        arrow_button.click()
    return wrapper


class Whatsapp:
    def __init__(self) -> None:
        # alistamos el driver
        self.options = Options()
        self.options.add_argument("user-data-dir=selenium")
        self.options.binary_location = const.path_chrome_bin  # viene de const.py
        self.driver = webdriver.Chrome(
            options=self.options, executable_path=const.path_chrome_driver)

        # abrimos whatsapp
        self.driver.get(const.whatsapp_url)
        self.driver.maximize_window()
        time.sleep(20)

    def search_contact(self, item: str) -> None:
        # buscamos el contacto
        search_box = self.driver.find_element(By.XPATH, const.search_input)
        search_box.send_keys(item)
        search_box.send_keys(Keys.ENTER)

    def send_message(self, message: str) -> None:
        # bucamos el input de mensaje y mandamos el mensaje
        message_box = self.driver.find_element(By.XPATH, const.message_input)
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

    @find_attach_input
    def send_image(self, image:str) -> None:
        # buscamos el input de imagen
        boton_imagen = self.driver.find_element(By.XPATH, const.image_input)
        boton_imagen.send_keys(f"{const.path_images}/{image}")

    @find_attach_input
    def send_video(self, video: str) -> None:
        #en contruccion
        # buscamos el input de video
        boton_imagen = self.driver.find_element(By.XPATH, const.image_input)
        boton_imagen.send_keys(f"{const.path_images}/{video}")

        