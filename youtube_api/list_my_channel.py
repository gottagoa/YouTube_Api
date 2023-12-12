# from googleapiclient.discovery import build
# from google.oauth2.credentials import Credentials
# # Credentials для представления учетных данных пользователя.


# '''
# build - это функция из библиотеки google-api-python-client, которая предоставляет удобный способ
# создания объектов API для взаимодействия с конкретными API Google (например, YouTube Data API). 
# Эта функция возвращает объект, представляющий API, с которым вы можете взаимодействовать.
# Эта функция build создает объект API, который предоставляет набор методов для выполнения 
# запросов к конкретному API. Например, для YouTube API, созданный объект youtube предоставит методы для
# выполнения запросов 
# к видео, каналам и другим ресурсам, определенным в YouTube Data API.
# '''

# def get_my_channel_info(api_key, credentials):
#     youtube = build('youtube', 'v3', developerKey=api_key, credentials=credentials)
    
#     request = youtube.channels().list(
#         part='snippet,contentDetails,statistics',
#         mine=True
#     )

#     response = request.execute()
#     return response
# '''
# Здесь youtube.videos().list - это метод YouTube API для выполнения запросов к видео. 
# Методы и параметры будут зависеть от конкретной службы и версии API.
# '''

# # Укажите свой API-ключ и объект Credentials (аутентификация пользователя)
# api_key = 'YOUR_API_KEY'
# user_credentials = Credentials.from_authorized_user_file('path/to/credentials.json')

# '''
# from_authorized_user_file - это метод встроенного класса Credentials из библиотеки google-auth-oauthlib.
# Этот метод используется для создания объекта 
# Credentials на основе данных об авторизованном пользователе, сохраненных в файле.
# '''
# # Укажите свой API-ключ и объект Credentials (аутентификация пользователя)


# channel_info = get_my_channel_info(api_key, user_credentials)
# print(channel_info)
# # В этом примере file_path - это путь к файлу, в котором хранятся учетные данные пользователя
# # (такой файл обычно создается в процессе получения учетных данных с использованием OAuth 2.0). 
# # Метод from_authorized_user_file создает объект Credentials,
# # который может быть использован для аутентификации пользователя при выполнении запросов к API.