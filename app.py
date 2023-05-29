import os
import random
from controllers.Whatsapp import Whatsapp
from controllers.Drive import Drive
from utils.const import DRIVE_URL_MULTIMEDIA


def show_list(l: list) -> None:
    for i, j in zip(l, range(1, len(l)+1)):
        print(f'{j} {i.get("name")}')
    print()


def get_multimedia_carpet(multimedia: dict) -> dict:
    pesos = [80, 20]
    print("SELECCIONANDO MULTIMEDIA")
    carpet = random.choices(list(multimedia.keys()), weights=pesos)[0]
    return multimedia.get(carpet)


def get_multimedia(multimedia: dict):
    multimedia_items = drive.get_items(id_carpet=multimedia.get('id'))
    multimedia_items = random.sample(multimedia_items, 3)
    return multimedia_items


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
    multimedia, txts = {}, []

    for item in items_carpets:
        if '.' in item.get('name'):
            txts.append(item)
        else:
            multimedia[item.get('name')] = item

    multimedia_carpet = get_multimedia_carpet(multimedia)
    multimedia_items = get_multimedia(multimedia_carpet)
    multimedia_url = DRIVE_URL_MULTIMEDIA.format(multimedia_items[0].get('id'))

    txt = random.choice(txts)
    txt_content = drive.service.files().get_media(
        fileId=txt.get('id')).execute().decode('utf-8')
    whatsapp.search_contact('68638319')
    whatsapp.send_message(txt_content)
    whatsapp.send_image(multimedia_url)


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
