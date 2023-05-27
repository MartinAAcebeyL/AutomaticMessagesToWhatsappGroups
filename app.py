from controllers.Whatsapp import Whatsapp
from controllers.Drive import Drive
import os
import time
import random
import io


def show_list(l: list) -> None:
    for i, j in zip(l, range(1, len(l)+1)):
        print(f'{j} {i.get("name")}')
    print()


def default():
    drive = Drive()
    whatsapp = Whatsapp()
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
    whatsapp.quit_driver()


def choose_carpet():
    drive = Drive()
    whatsapp = Whatsapp()
    items = drive.get_items(id_carpet=os.getenv('ID_CARPET'), folders=True)

    while True:
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
        aux = input("Desea enviar otro mensaje? (y/n)\n")
        if aux == 'n':
            break

    print("Saliendo...")
    whatsapp.quit_driver()


def exit_():
    drive = Drive()
    show_list(drive.get_carpets())
    print("exit")


if __name__ == "__main__":
    while True:
        opcion = int(input(
            "1. Correr el script por defecto\n2. Seleccion una nueva carpeta\n3. Salir\n\n"))

        acciones = {
            1: default,
            2: choose_carpet,
            3: exit_
        }

        acciones[opcion]()
        
        if opcion == 3:
            break
