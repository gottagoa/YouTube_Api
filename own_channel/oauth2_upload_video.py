import os
import socket
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


SCOPES=[
    'https://www.googleapis.com/auth/youtube.force-ssl',
    'https://www.googleapis.com/auth/userinfo.profile',
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/userinfo.email'
]

CLIENT_SECRET_FILE='/Users/ajzanylsabdanbekova/Desktop/python/youtubeapi/own_channel/client_secret.json'
CHANNEL_ID='UCrOYjS2VKmDAy39AI2BCfKw'


flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
flow.redirect_uri = "https://oauth.pstmn.io/v1/callback"
credentials = flow.run_local_server()


token_file='token.json'
with open(token_file, 'w') as token:
    token.write(credentials.to_json())

youtube=build('youtube', 'v3', credentials=credentials)

def upload_video(youtube, file_path, title, description):
    request_body={
        'snippet':{
            'title': title,
            'description':description,
            'tags': ['python', 'youtube', 'api'],
            'categoryId': '27'
        },
        'status': {
            'privacyStatus': 'private',
        }
    }

    media_file=MediaFileUpload(file_path)

    response=(
        youtube.videos()
        .insert(
            part='snippet, status',
            body=request_body,
            media_body=media_file,
        )
        .execute()
    )
    print(f"Video id {response['id']} was succesfully uploaded.")

file_path='/Users/ajzanylsabdanbekova/Desktop/lesson4-списки.mov'
title="Онлайн урок 4-Списки. Методы списков. Индексы."
description='В онлайн уроке раскрыта тема работы и конструкции списков в Python, а также решены задачи'

# upload_video(youtube, file_path, title, description)

