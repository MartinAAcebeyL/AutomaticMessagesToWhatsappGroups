import os


def remove_files():
    carpeta = 'temp'
    archivos = os.listdir(carpeta)
    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_archivo):
            os.remove(ruta_archivo)

    print("ARCHIVOS ELIMINADOS ...")
