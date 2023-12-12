# '''
# List (by Channel ID):

# Описание: Этот запрос используется для получения информации о канале на YouTube, идентифицируемом уникальным 
# идентификатором канала, известным как Channel ID.
# Пример использования: Вы можете передать Channel ID в запросе и получить данные, такие как заголовок канала, описание, 
# дата создания и другие сведения о канале.
# '''

# from googleapiclient.discovery import build

# def get_channel_info_by_id(api_key, channel_id):
#     youtube = build('youtube', 'v3', developerKey=api_key)
    
#     request = youtube.channels().list(
#         part='snippet,contentDetails,statistics',
#         id=channel_id
#     )

#     response = request.execute()
#     return response

# # Укажите свой API-ключ и Channel ID
# api_key = 'YOUR_API_KEY'
# channel_id = 'CHANNEL_ID'

# channel_info = get_channel_info_by_id(api_key, channel_id)
# print(channel_info)


# text = '-? I-love-Bishkek ?'
# # Будем решать двумя шагами
# # 1. В новую строку добавляем текст без символов в начале и конце
# # print(len(text))
# new_text= text[3:18]
# print(new_text)
# # # 2. Убираем дефисы внутри предложения
# print(new_text.replace('-', ' '))