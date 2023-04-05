from Whatsapp import Whatsapp
from Drive import Drive
import os


# whatsapp.search_contact("73883448")
# whatsapp.send_message("hola bro")
# whatsapp.quit_driver()
def show_list(l: list) -> None:
    for i, j in zip(l, range(1, len(l)+1)):
        print(f'{j} {i}')


def default():
    # whatsapp = Whatsapp()
    drive = Drive()
    show_list(drive.get_items(id_carpet=os.getenv('ID_CARPET')))
    # show_list(drive.get_items(id_carpet='1LqdGWDNugEp2i5cgTbYZTjuB8_UfwR2R'))


def choose_carpet():
    drive = Drive()
    show_list(drive.get_items(folders=True))


def exit_():
    drive = Drive()
    show_list(drive.get_carpets())
    print("exit")


if __name__ == "__main__":
    opcion = int(input("""
    1. Correr el script por defecto
    2. Seleccion una nueva carpeta
    3. Salir\n"""))

    acciones = {
        1: default,
        2: choose_carpet,
        3: exit_
    }

    acciones[opcion]()
