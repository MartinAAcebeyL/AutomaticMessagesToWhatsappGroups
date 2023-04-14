from Whatsapp import Whatsapp
from Drive import Drive
import os
import time
import random
import io

# https://drive.google.com/drive/folders/1ZXRhEGp03TjW9JLs4hQkfFDHg56yqjk6?usp=share_link


def show_list(l: list) -> None:
    for i, j in zip(l, range(1, len(l)+1)):
        print(f'{j} {i}')


def default():
    drive = Drive()
    items = drive.get_items(id_carpet=os.getenv('ID_CARPET'), folders=True)

    for folder in items[:1]:
        print(folder)
        items_carpets = drive.get_items(id_carpet=folder.get('id'))
        # choose a txt
        txts = [i for i in items_carpets if '.' in i.get('name')]
        txt = random.choice(txts)
        txt_content = drive.service.files().get_media(
            fileId=txt.get('id')).execute()
        whatsapp = Whatsapp()
        whatsapp.search_contact('738834')
        whatsapp.send_message("😀")
        whatsapp.quit_driver()


def choose_carpet():
    drive = Drive()
    show_list(drive.get_items(folders=True))


def exit_():
    drive = Drive()
    show_list(drive.get_carpets())
    print("exit")


if __name__ == "__main__":
    whatsapp = Whatsapp()
    # whatsapp.search_contact('738834')
    # whatsapp.send_message("😀")
    whatsapp.quit_driver()

    # opcion = int(input("""
    # 1. Correr el script por defecto
    # 2. Seleccion una nueva carpeta
    # 3. Salir\n"""))

    # acciones = {
    #     1: default,
    #     2: choose_carpet,
    #     3: exit_
    # }

    # acciones[opcion]()
