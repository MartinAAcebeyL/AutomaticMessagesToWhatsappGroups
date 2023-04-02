from drive import Drive
from dotenv import load_dotenv
import os
load_dotenv()

if __name__ == "__main__":
    drive = Drive()
    id_carpet = os.getenv('ID_CARPET')
    carpets = drive.get_carpets()

    for carpet in carpets:
        print(carpet)