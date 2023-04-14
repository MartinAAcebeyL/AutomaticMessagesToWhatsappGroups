from dotenv import load_dotenv
import os
load_dotenv()

path_chrome_bin = "/bin/google-chrome"

path_chrome_driver = os.getenv('PATH_CHOROME_DRIVER')
path_firefox_driver = os.getenv('PATH_FIREFOX_DRIVER')
path_firefox_perfil = os.getenv('PATH_FIREFOX_PERFIL')

whatsapp_url = "https://web.whatsapp.com/"

# //*[@id = "side"]/div[1]/div/div/div[2]/div/div[1]
# /html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]/p
search_input = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p'
'/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]/p'

message_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
attach_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'
image_input = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input'

path_images = '/home/martindev/Descargas'

arrow_btn = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span'
