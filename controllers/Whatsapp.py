from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import utils.const as const
from selenium import webdriver
from selenium.webdriver.firefox.options import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains


def find_attach_input(function):
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
        print("INICIANDO WHATSAPP")
        # alistamos el driver
        """
        #PARA CHROME
        self.options = Options()
        self.options.add_argument("user-data-dir=selenium")
        self.driver = webdriver.Chrome(
        options=self.options, executable_path=const.path_chrome_driver)
        """
        self.profile = FirefoxProfile(const.path_firefox_perfil)
        self.driver = webdriver.Firefox(firefox_profile=self.profile, )
        # abrimos whatsapp
        self.driver.get(const.whatsapp_url)
        self.driver.maximize_window()
        time.sleep(20)

    def quit_driver(self) -> None:
        input("PRESIONE ENTER PARA CERRAR WHATSAPP: ")
        self.driver.quit()

    def search_contact(self, contact: str) -> None:
        print(f"BUSCANDO CONTACTO: {contact}")
        # buscamos el contacto
        search_box = self.driver.find_element(By.XPATH, const.search_input)
        search_box.click()

        actions = ActionChains(self.driver)
        for char in contact:
            actions.send_keys(char)
        actions.perform()

        # search_box.send_keys("738834")
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

    def send_message(self, message: str) -> None:
        print("ENVIANDO MENSAJE...")
        # bucamos el input de mensaje y mandamos el mensaje
        message_box = self.driver.find_element(By.XPATH, const.message_input)
        # message_box.send_keys(message)
        actions = ActionChains(self.driver)
        for char in message:
            actions.send_keys(char)
        actions.perform()
        message_box.send_keys(Keys.ENTER)
        time.sleep(2)

    @find_attach_input
    def send_image(self, image: str) -> None:
        print("ENVIANDO IMAGEN")
        # buscamos el input de imagen
        boton_imagen = self.driver.find_element(By.XPATH, const.image_input)
        boton_imagen.send_keys(f"{const.path_images}/{image}")

    @find_attach_input
    def send_video(self, video: str) -> None:
        print("ENVIANDO VIDEO")
        # en contruccion
        # buscamos el input de video
        boton_imagen = self.driver.find_element(By.XPATH, const.image_input)
        boton_imagen.send_keys(f"{const.path_images}/{video}")
