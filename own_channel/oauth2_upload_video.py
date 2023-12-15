import os
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES=['https://www.googleapis.com/auth/youtube.upload']

CLIENT_SECRET_FILE='client_secret.json'
CHANNEL_ID='UCrOYjS2VKmDAy39AI2BCfKw'

flow=InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials=flow.run_console()

token_file='token.json'
with open(token_file, 'w') as token:
    token.write(credentials.to_json())

youtube=build('youtube', 'v3', credentials=credentials)

def upload_video(youtube, file_path, title, description):
    request_body={
        'snippet':{
            'title': title,
            'description':'description',
            'tags': ['python', 'youtube', 'api'],
            'categoryId': '22'
        }
    }
