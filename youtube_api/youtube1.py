# import os
# import google_auth_oauthlib.flow
# import googleapiclient.discovery
# import googleapiclient.errors
# from googleapiclient.discovery import build
# import json

# # необходимо сначала установить библиотеку google-api-python-client: pip install google-api-python-client

# API_KEY=''
# # здесь представле ключ пользователя, зарегистрировавшийся в google cloude platform console


# def get_service():
#     service=build('youtube', 'v3', developerKey=API_KEY)
#     return service

# # Get channel info (title, desc, stats)
# def get_channel_info(channel_id=''):
#     r=get_service().channels().list(id=channel_id, part='snippet, statistics').execute()
#     print(r['items'][0]['snippet']['title'])
#     print(r['items'][0]['statistics']['viewcount'])


# # Get video info(title, stats, desc)
# def get_video_info(video_id=''):
#     r=get_service().videos().list(id=video_id, part='snippet,statistics').execute()
#     print(r['items'][0]['snippet']['title'])
#     print(r['items'][0]['statistics']['viewcount'])


# if __name__=='__main__' :
#     # get_channel_info('')
#     get_video_info('')