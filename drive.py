import os
import os.path
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
creds = None

if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

if not creds or not creds.valid:

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# try:
#     service = build('drive', 'v3', credentials=creds)
#     ##### OPERACION DE LISTADO DE ARCHIVOS #############
#     results = service.files().list(fields="nextPageToken, files(id,name)").execute()
#     items = results.get('files', [])
#     if not items:
#         print("No hay items")
#     for item in items:
#         print(f"name {item['name']} , id {item['id']}")
# except HttpError as error:
#     print(f'Ocurrió un error {error}')


# Autenticar aplicación para acceder a datos de Google Drive
creds = Credentials.from_authorized_user_file(
    'token.json', SCOPES)

# ID del archivo de texto a leer
file_id = os.getenv('id_txt')

# Crear objeto de servicio de Google Drive
service = build('drive', 'v3', credentials=creds)

# Obtener información del archivo de texto
file = service.files().get(fileId=file_id).execute()

# Descargar contenido del archivo de texto
content = service.files().get_media(fileId=file_id).execute()

# Convertir contenido a cadena de texto
text = content.decode('utf-8')

# Imprimir texto
print(text)
