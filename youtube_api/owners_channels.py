from googleapiclient.discovery import build

def get_channels_managed_by_content_owner(api_key, content_owner_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        managedByMe=True,
        onBehalfOfContentOwner=content_owner_id
    )

    response = request.execute()
    return response

# Укажите свой API-ключ и идентификатор владельца контента
api_key = 'YOUR_API_KEY'
content_owner_id = 'CONTENT_OWNER_ID'

channels_info = get_channels_managed_by_content_owner(api_key, content_owner_id)
print(channels_info)
