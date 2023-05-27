from controllers.Whatsapp import Whatsapp
from controllers.Drive import Drive
import os
import random


def show_list(l: list) -> None:
    for i, j in zip(l, range(1, len(l)+1)):
        print(f'{j} {i.get("name")}')
    print()


def default():
    items = drive.get_items(id_carpet=os.getenv('ID_CARPET'), folders=True)

    for folder in items[:-1]:
        print(f"item: {folder.get('name')}".center(100, ' '))
        items_carpets = drive.get_items(id_carpet=folder.get('id'))
        # choose a txt
        txts = [i for i in items_carpets if '.' in i.get('name')]
        txt = random.choice(txts)
        txt_content = drive.service.files().get_media(
            fileId=txt.get('id')).execute().decode('utf-8')
        whatsapp.search_contact('68638319')
        whatsapp.send_message(txt_content)


def choose_carpet():
    items = drive.get_items(id_carpet=os.getenv('ID_CARPET'), folders=True)
    print("Selecciona una carpeta")
    show_list(items)
    folder = input()
    folder = items[int(folder)-1]
    items_carpets = drive.get_items(id_carpet=folder.get('id'))
    txts = [i for i in items_carpets if '.' in i.get('name')]
    txt = random.choice(txts)
    txt_content = drive.service.files().get_media(
        fileId=txt.get('id')).execute().decode('utf-8')
    whatsapp.search_contact('68638319')
    whatsapp.send_message(txt_content)


whatsapp = Whatsapp()
drive = Drive()

if __name__ == "__main__":
    while True:
        opcion = int(input(
            "1. Correr el script por defecto\n2. Seleccion una nueva carpeta\n3. Salir\n\n"))

        if opcion == 3:
            print("Saliendo...")
            whatsapp.quit_driver()
            break

        acciones = {
            1: default,
            2: choose_carpet,
        }

        acciones[opcion]()
