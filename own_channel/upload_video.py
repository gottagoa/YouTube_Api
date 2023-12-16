# #!/usr/bin/python

# import http.client
# import os
# import random
# import sys
# import time

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# from googleapiclient.http import MediaFileUpload

# http.client.RETRIES = 1
# MAX_RETRIES = 10

# RETRIABLE_EXCEPTIONS = (IOError, http.client.NotConnected,
#     http.client.IncompleteRead, http.client.ImproperConnectionState,
#     http.client.CannotSendRequest, http.client.CannotSendHeader,
#     http.client.ResponseNotReady, http.client.BadStatusLine)

# RETRIABLE_STATUS_CODES=[500,502,503,504]

# CLIENT_SECRETS_FILE="client_secrets.json"

# YOUTUBE_UPLOAD_SCOPE="https://www.googleapis.com/auth/youtube.upload"
# YOUTUBE_API_SERVICE_NAME= "youtube"
# YOUTUBE_API_VERSION= "v3"


# MISSING_CLIENT_SECRETS_MESSAGE= """
# WARNING: Please configure OAuth 2.0

# To make this simple run you well need to populate the client_secrets.json file found at:
# with information from the API Console
# https://console.cloud.google.com/

# For more information about the clients_secrets.json file format, please visit:
# https://developers.google.com/api-client-library/python/guide/aaa_client_secrets

# """ %os.path.abspath(os.path.join(os.path.dirname(__file__), CLIENT_SECRETS_FILE))

# VALID_PRIVACY_SETTINGS=('public', 'private', 'unlisted')

# def get_authenticated_service(args):
#     token_file='token.json' 
#     # Проверка наличия файла token.json. Если файл существует, код попытается загрузить учетные данные из него.
#     creds=None
#     if os.path.exists(token_file):
#         creds=Credentials.from_authorized_user_file(token_file)
#         # если файл существует, и он содержит действительные учетные данные, они будут загружены

#     if not creds or not creds.valid:
#         # Если учетные данные не существуют, недействительны или устарели, выполняется следующий блок кода:
#         if creds and creds.expired and creds.refresh_token:
#             # Если учетные данные устарели и у пользователя есть refresh token, происходит попытка обновления учетных данных.
#             creds.refresh(Request())
#         else:
#             flow=InstalledAppFlow.from_client_secrets_file(
#                 CLIENT_SECRETS_FILE, [YOUTUBE_UPLOAD_SCOPE]
#             )
#             # В противном случае, создается объект InstalledAppFlow с использованием данных из файла CLIENT_SECRETS_FILE 
#             # (предполагается, что это JSON-файл с клиентскими секретами OAuth 2.0) и запускается локальный веб-сервер 
#             # (flow.run_local_server(port=0)), 
#             # чтобы пользователь мог войти в свой аккаунт Google и предоставить необходимые разрешения.
#             creds=flow.run_local_server(port=0)
#         #     нулевой порт указывает на то, что при запуске программа сама выберет свободный порт,
#         # чтобы не было конфликтов портов с другими приложениями
#         with open(token_file, 'w') as token:
#             token.write(creds.to_json())
#             # После успешной аутентификации и получения учетных данных, они сохраняются в файл token.json 
#             # для использования при следующих запусках приложения

#     return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=creds)
# # создается объект YouTube API с использованием учетных данных пользователя, готовых к использованию в запросах к API.

# # Таким образом, весь этот блок кода обеспечивает процесс аутентификации пользователя и обработки учетных данных, 
# # чтобы приложение могло взаимодействовать с YouTube API от его имени.
# def initialize_upload(youtube, options):
#     tags = None
#     if options.keywords:
#         tags = options.keywords.split(",")

#     body = dict(
#         snippet=dict(
#             title=options.title,
#             description=options.description,
#             tags=tags,
#             categoryId=options.category
#         ),
#         status=dict(
#             privacyStatus=options.privacyStatus
#         )
#     )

#     insert_request = youtube.videos().insert(
#         part=",".join(body.keys()),
#         body=body,
#          media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
#     )

#     resumable_upload(insert_request)

# def resumable_upload(insert_request):
#     response = None
#     error = None
#     retry = 0
#     while response is None:
#         try:
#             print("Uploading file...")
#             status, response = insert_request.next_chunk()
#             if response is not None:
#                 if 'id' in response:
#                     print("Video id '%s' was successfully uploaded." % response['id'])
#                 else:
#                     exit("The upload failed with an unexpected response: %s" % response)
#         except HttpError as e:
#             if e.resp.status in RETRIABLE_STATUS_CODES:
#                 error = "A retriable HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
      
#             else:
#                 raise

#             except RETRIABLE_EXCEPTIONS as e:
#                 error = "A retriable error occurred: %s" % e

#             if error is not None:
#                 print(error)
#                 retry += 1
#                 if retry > MAX_RETRIES:
#                     exit("No longer attempting to retry.")

#                 max_sleep = 2 ** retry
#                 sleep_seconds = random.random() * max_sleep
#                 print("Sleeping %f seconds and then retrying..." % sleep_seconds)
#                 time.sleep(sleep_seconds)


# if __name__ == '__main__':
#     # Ваш существующий код...
#     args = argparser.parse_args()

#     if not os.path.exists(args.file):
#         exit("Please specify a valid file using the --file= parameter.")

#     youtube = get_authenticated_service()
#     try:
#         initialize_upload(youtube, args)
#     except HttpError as e:
#         print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
