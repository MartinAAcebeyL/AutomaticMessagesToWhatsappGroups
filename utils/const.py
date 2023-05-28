from dotenv import load_dotenv
import os
load_dotenv()

PATH_CHROME_BIN = "/bin/google-chrome"

PATH_CHROME_DRIVER = os.getenv('PATH_CHOROME_DRIVER')
PATH_FIREFOX_DRIVER = os.getenv('PATH_FIREFOX_DRIVER')
PATH_FIREFOX_PERFIL = os.getenv('PATH_FIREFOX_PERFIL')

WHATSAPP_URL = "https://web.whatsapp.com/"

SEARCH_INPUT = '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]'
MESSAGE_INPUT = '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'

ATTACH_INPUT = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'
IMAGE_INPUT = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input'

PATH_IMAGES = '/home/martindev/Descargas'

ARROW_BTN = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span'
