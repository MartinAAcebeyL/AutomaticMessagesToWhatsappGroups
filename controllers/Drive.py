import os
import random
import time
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from dotenv import load_dotenv
from googleapiclient.http import MediaIoBaseDownload

load_dotenv()


class Drive:
    def __init__(self) -> None:
        self.SCOPES = [os.getenv('DRIVE_SCOPE')]
        self.creds = None
        token_path = 'token.json'
        if os.path.exists(token_path):
            self.creds = Credentials.from_authorized_user_file(
                token_path, self.SCOPES)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())

        self.service = build('drive', 'v3', credentials=self.creds)

    def get_carpets(self) -> list:
        items = self.service.files().list(
            fields="nextPageToken, files(id,name)").execute().get('files', [])

        carpets = []
        for item in items:
            if '.' not in item['name']:
                carpets.append(item)
        return sorted(carpets, key=lambda x: x['name'])

    def get_items(self, id_carpet: str = None, folders: bool = False, t: str = None) -> list:
        if id_carpet:
            items = self.service.files().list(
                fields="nextPageToken, files(id,name)", q=f"'{id_carpet}' in parents").execute().get('files', [])
        else:
            items = self.service.files().list(
                fields="nextPageToken, files(id,name)").execute().get('files', [])

        if folders:
            items = [item for item in items if '.' not in item['name']]
        elif t:
            items = [item for item in items if f'.{t}' in item['name']]

        return sorted(items, key=lambda x: x['name'])

    def download_file(self, file_id: str, file_name: str) -> None:
        request = self.service.files().get_media(fileId=file_id)
        fh = open(f"temp/{file_name}", 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()

    def get_multimedia_folder(self, multimedia: dict) -> dict:
        pesos = [80, 20]
        print("SELECCIONANDO MULTIMEDIA")
        carpet = random.choices(list(multimedia.keys()), weights=pesos)[0]
        return multimedia.get(carpet)

    def get_multimedia(self, carpeta: dict, cantidad: int = 3) -> list:
        items = self.get_items(id_carpet=carpeta.get('id'))
        items = random.sample(items, cantidad)
        return items

    def separar_carpetas_txt(self, items: list) -> list:
        folders, txts = {}, []
        for item in items:
            if '.' in item.get('name'):
                txts.append(item)
            else:
                folders[item.get('name')] = item
        return folders, txts

    def multimadia_y_txts(self, items_principal_carpets: dict) -> list:
        multimedia, txts = self.separar_carpetas_txt(items_principal_carpets)
        # Seleccionar carpeta de multimedia y descargando multimedia
        multimedia_folder = self.get_multimedia_folder(multimedia)
        cantitad_items = 3 if multimedia_folder.get('name') == 'fotos' else 1
        multimedia_items = self.get_multimedia(
            multimedia_folder, cantitad_items)

        multimedia = []
        for item in multimedia_items:
            self.download_file(item.get('id'), item.get('name'))
            multimedia.append(item.get('name'))
            time.sleep(0.5)
        print("DESCARGA COMPLETA")
        

        # Seleccionando un txt
        txt = random.choice(txts)
        txt_content = self.service.files().get_media(
            fileId=txt.get('id')).execute().decode('utf-8')
        return multimedia, txt_content
