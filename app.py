import os
from controllers.Whatsapp import Whatsapp
from controllers.Drive import Drive
from utils.utils import remove_files, show_list, read_txt


def default():
    folders = drive.get_items(id_carpet=os.getenv('ID_CARPET'), folders=True)
    for folder in folders[:-2]:
        print(f"item: {folder.get('name')}".center(100, ' '))
        items_folder = drive.get_items(id_carpet=folder.get('id'))
        for contacto in read_txt():
            print(f"BUSCANDO CONTACTO: {contacto}")
            multimedia, txt = drive.multimadia_y_txts(items_folder)
            whatsapp.search_contact(contacto)
            whatsapp.send_message(txt)
            for i in multimedia:
                whatsapp.send_multimedia(i)
            remove_files()
            print()


def choose_carpet():
    principal_carpets = drive.get_items(
        id_carpet=os.getenv('ID_CARPET'), folders=True)
    print("SELECCIONA UNA CARPETA:")
    show_list(principal_carpets)
    folder = input()
    folder = principal_carpets[int(folder)-1]
    items_folder = drive.get_items(id_carpet=folder.get('id'))
    for contacto in read_txt():
        print(f"\nBUSCANDO CONTACTO: {contacto}")
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
