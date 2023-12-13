# from googleapiclient.discovery import build
# from google.oauth2.credentials import Credentials
# import os
# # находим продолжительность видео и всего плейлиста
# api_key='AIzaSyCbXuG-eNeZRxtv8Zv9lulG37HpL03Evyk'

# youtube=build('youtube', 'v3', developerKey=api_key)
# pl_request=youtube.playlistItems().list(
#     part='contentDetails',
#     playlistId='Pl-osiE80TeTsWmV9i9c58mdDCSskIFdD'
# )

# pl_response=pl_request.execute()

# vid_ids=[]
# for item in pl_response['items']:
#     vid_ids.append(item['contentDetails']['videoId'])

# print(','.join(vid_ids))

