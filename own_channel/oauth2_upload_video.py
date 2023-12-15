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
        },

        "status": {
            "privacyStatus": "private",  # Установите "public" для публичной загрузки
        },
    }

    media_file = MediaFileUpload(file_path)

    response = (
        youtube.videos()
        .insert(
            part="snippet,status",
            body=request_body,
            media_body=media_file,
        )
        .execute()
    )

    print("Video id '{}' was successfully uploaded.".format(response["id"]))

# Пример использования функции загрузки видео
video_file_path = "path/to/your/video.mp4"
video_title = "Your Video Title"
video_description = "Your video description goes here."

upload_video(youtube, video_file_path, video_title, video_description)
