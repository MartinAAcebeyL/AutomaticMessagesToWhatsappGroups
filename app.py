import os
import random
from controllers.Whatsapp import Whatsapp
from controllers.Drive import Drive
from utils.utils import remove_files, show_list, read_txt


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
    principal_carpets = drive.get_items(
        id_carpet=os.getenv('ID_CARPET'), folders=True)
    print("SELECCIONA UNA CARPETA:")
    show_list(principal_carpets)
    folder = input()
    folder = principal_carpets[int(folder)-1]
    for contacto in read_txt():
        print(f"\nBUSCANDO CONTACTO: {contacto}")
        items_folder = drive.get_items(id_carpet=folder.get('id'))
        multimedia, txt = drive.multimadia_y_txts(items_folder)
        whatsapp.search_contact(contacto)
        whatsapp.send_message(txt)
        for i in multimedia:
            whatsapp.send_multimedia(i)
        remove_files()


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
