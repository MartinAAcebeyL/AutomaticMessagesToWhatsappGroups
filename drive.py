from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
# Autenticar aplicación para acceder a datos de Google Drive
creds = Credentials.from_authorized_user_file(
    'credentials.json', SCOPES)

# ID del archivo de texto a leer
file_id = '1YhrGJziZknNQU0sFOF7RX0hmocChwEoO'

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

