from Whatsapp import Whatsapp
from Drive import Drive

whatsapp = Whatsapp()
drive = Drive()

whatsapp.search_contact("73883448")
whatsapp.send_message("hola bro")
whatsapp.quit_driver()
