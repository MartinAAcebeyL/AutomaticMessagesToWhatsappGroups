from .controllers.Whatsapp import Whatsapp
from .controllers.Drive import Drive
import os
import time
import random
import io

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
            fileId=txt.get('id')).execute().decode('utf-8')
        whatsapp = Whatsapp()
        whatsapp.search_contact('738834')
        whatsapp.send_message(u"\u1F625")
        whatsapp.quit_driver()


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

"""
\U0001F6A5 ¡Atención a todos los amantes de la tecnología! \U0001F6A5

¡Les presentamos el nuevo Smartwatch DW35 PRO año 2022! \U0001F60E

Con este increíble dispositivo, podrás revisar tus llamadas, mensajes y notificaciones de WhatsApp, Facebook y más, ¡además de tener un asistente de voz! \U0001F62E

Pero eso no es todo, también podrás medir tu presión, oxígeno en la sangre, temperatura y ritmo cardíaco. ¡Y controlar tu proceso en cualquier deporte! \U0001F3CB \U0001F3CA \U0001F93E

¡Y no te preocupes por la duración de la batería! ¡Tiene una duración de 3 a 5 días! \U0001F4AA

Viene en una caja sellada con 2 diferentes correas (silicona y naylon), diferentes fondos de pantalla, 3 diferentes tipos de menú y una pantalla de 1.75 pulgadas HD Full touch. ¡También es resistente al polvo y al agua! \U0001F4A6

Y lo mejor de todo es que hacemos envíos a todas las ciudades dentro del territorio nacional. ¿Qué estás esperando para tener el tuyo?

¡Consulta cualquier duda en nuestro inbox o por Whatsapp en el siguiente enlace! wa.link/bzilrw
¡No te quedes sin tu Smartwatch DW35 PRO! \U0001F60D\U0001F4BB\U0001F4F1
"""