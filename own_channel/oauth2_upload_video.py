import os
import socket
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


SCOPES=['https://www.googleapis.com/auth/youtube.upload']

CLIENT_SECRET_FILE='/Users/ajzanylsabdanbekova/Desktop/python/youtubeapi/own_channel/client_secret.json'
CHANNEL_ID='UCrOYjS2VKmDAy39AI2BCfKw'


flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
flow.redirect_uri = "http://localhost:9000"
credentials = flow.run_local_server()


token_file='token.json'
with open(token_file, 'w') as token:
    token.write(credentials.to_json())

youtube=build('youtube', 'v3', credentials=credentials)

# def upload_video(youtube, file_path, title, description):
#     request_body={
#         'snippet':{
#             'title': title,
#             'description':description,
#             'tags': ['python', 'youtube', 'api'],
#             'categoryId': '27'
#         },
#         'status': {
#             'privacyStatus': 'private',
#         }
#     }

#     media_file=MediaFileUpload(file_path)

#     response=(
#         youtube.videos()
#         .insert(
#             part='snippet, status',
#             body=request_body,
#             media_body=media_file,
#         )
#         .execute()
#     )
#     print(f"Video id {response['id']} was succesfully uploaded.")

# file_path='/Users/ajzanylsabdanbekova/Desktop/lesson4-списки.mov'
# title="Онлайн урок 4-Списки. Методы списков. Индексы."
# description='В онлайн уроке раскрыта тема работы и конструкции списков в Python, а также решены задачи'

# upload_video(youtube, file_path, title, description)

def upload_thumbnail(self, video_id, file_path):
        print('Uploading thumbnail...')
        request = self.youtube.thumbnails().set(
            videoId=video_id,
            media_body=file_path
        )
        response = request.execute()
        print(response)

def upload_video(self, file_path, video_content):
    body = dict(
        snippet=dict(
            title=video_content.title,
            description=video_content.description,
            tags=video_content.tags,
            categoryId=video_content.category_id
        ),

        status=dict(
            privacyStatus=video_content.privacy_status
        )
    )

    insert_request = self.youtube.videos().insert(
        part=",".join(body.keys()),
        body=body,
        media_body= MediaFileUpload(
            file_path, chunksize=-1, resumable=True)
    )

    video_id = self.resumable_upload(insert_request)
    self.upload_thumbnail(video_id, 'files/youtube/thumbnail.png')