from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import utils.const as const
from selenium import webdriver
from selenium.webdriver.firefox.options import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

    
def find_attach_input(function):
    def wrapper(self, *args, **kwargs):
        # buscamos el input de adjuntar
        adjuntar = self.driver.find_element(By.XPATH, const.ATTACH_INPUT)
        adjuntar.click()
        function(self, args[0])
        # buscamos el boton de enviar
        arrow_button = self.driver.find_element(By.XPATH, const.ARROW_BTN)
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
        options=self.options, executable_path=const.PATH_CHROME_DRIVER)
        """
        options = Options()
        options.set_preference("browser.download.folderList", 2)
        options.set_preference(
            "browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.dir",
                               "../tempo/")
        options.set_preference(
            "browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

        self.profile = FirefoxProfile(const.PATH_FIREFOX_PERFIL)
        self.driver = webdriver.Firefox(
            firefox_profile=self.profile, options=options)
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
        message_box = self.driver.find_element(By.XPATH, const.MESSAGE_INPUT)
        # message_box.send_keys(message)
        actions = ActionChains(self.driver)
        for char in message:
            actions.send_keys(char)
        actions.perform()
        message_box.send_keys(Keys.ENTER)
        time.sleep(2)

    # @find_attach_input
    def send_image(self, image: str) -> None:
        print("ENVIANDO IMAGEN...")
        print(image)
        self.driver.get(image)
        # Ajusta el tiempo máximo de espera según sea necesario
        espera = WebDriverWait(self.driver, 60)
        espera.until(EC.url_contains("accounts.google.com"))

        # buscamos el input de imagen
        # boton_imagen = self.driver.find_element(By.XPATH, const.IMAGE_INPUT)
        # boton_imagen.send_keys(f"{const.PATH_IMAGES}/{image}")
        # boton_imagen.send_keys(image)

    @find_attach_input
    def send_video(self, video: str) -> None:
        print("ENVIANDO VIDEO")
        # en contruccion
        # buscamos el input de video
        boton_imagen = self.driver.find_element(By.XPATH, const.IMAGE_INPUT)
        boton_imagen.send_keys(f"{const.PATH_IMAGES}/{video}")
