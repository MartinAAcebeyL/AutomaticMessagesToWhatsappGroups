import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from dotenv import load_dotenv

load_dotenv()


class Drive:
    def __init__(self) -> None:
        self.SCOPES = [os.getenv('DRIVE_SCOPE')]
        self.creds = None
        token_path = 'drive/token.json'
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
        return carpets

    def get_items(self, id_carpet: str) -> list:
        items = self.service.files().list(
            fields="nextPageToken, files(id,name)", q=f"'{id_carpet}' in parents").execute().get('files', [])
        return items

    def show_txt(self):
        pass
