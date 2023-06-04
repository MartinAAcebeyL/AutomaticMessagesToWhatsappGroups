import os


def remove_files():
    carpeta = 'temp'
    archivos = os.listdir(carpeta)
    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_archivo):
            os.remove(ruta_archivo)

    print("ARCHIVOS ELIMINADOS ...")


def read_txt() -> list:
    path = "contacts.txt"
    with open(path, 'r') as archivo:
        contenido = archivo.read()
    return contenido.split('\n')


def show_list(l: list) -> None:
    for i, j in zip(l, range(1, len(l)+1)):
        print(f'{j} {i.get("name")}')
    print()
