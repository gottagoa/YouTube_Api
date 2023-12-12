# from googleapiclient.discovery import build

# def get_channel_info_by_username(api_key, username):
#     youtube = build('youtube', 'v3', developerKey=api_key)
    
#     request = youtube.channels().list(
#         part='snippet,contentDetails,statistics',
#         forUsername=username
#     )

#     response = request.execute()
#     return response

# # Укажите свой API-ключ и YouTube Username
# api_key = 'YOUR_API_KEY'
# youtube_username = 'YOUTUBE_USERNAME'

# channel_info = get_channel_info_by_username(api_key, youtube_username)
# print(channel_info)
