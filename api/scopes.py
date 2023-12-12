'''
при использовании регистрации через OAUTH 2.0 необходимо указывать области разрешения(scopes)
для получения данных. В обратном случае, при использовании API-ключ (developerKey) для аутентификации,
и при использовании API-ключа не требуется указывать области (scopes),
API-ключ предоставляет доступ к общедоступным данным и не требует пользователя предоставлять разрешения. 
Однако, при использовании API-ключа, есть ограничения, например, 
вы не сможете получить доступ к личным данным пользователя или взаимодействовать с его каналом в интерактивном режиме.

https://www.googleapis.com/auth/youtube	Управляйте своим аккаунтом YouTube
https://www.googleapis.com/auth/youtube.channel-memberships.creator	Просматривайте список ваших текущих активных участников канала, их текущий уровень и время, когда они стали участником.
https://www.googleapis.com/auth/youtube.force-ssl	Просматривайте, редактируйте и безвозвратно удаляйте свои видео, рейтинги, комментарии и подписи на YouTube.
https://www.googleapis.com/auth/youtube.readonly	Просмотрите свой аккаунт YouTube
https://www.googleapis.com/auth/youtube.upload	Управляйте своими видео на YouTube
https://www.googleapis.com/auth/youtubepartner	Просмотр и управление своими объектами и связанным контентом на YouTube
https://www.googleapis.com/auth/youtubepartner-channel-audit

'''

# pip install google-api-python-client
# from google_auth_oauthlib.flow import InstalledAppFlow
# SCOPES = ['https://www.googleapis.com/auth/youtube.readonly', 'https://www.googleapis.com/auth/youtube.upload']

# flow = InstalledAppFlow.from_client_secrets_file(
#     'client_secret.json',  # Замените на путь к вашему файлу с секретами
#     SCOPES
# )
# credentials = flow.run_local_server(port=0)

'''
В этом примере SCOPES представляет список требуемых областей. Пользователь будет запрошен дать разрешение 
на доступ к данным, соответствующим этим областям.

Используйте токен доступа:
Получив токен доступа, вы можете использовать его для аутентификации запросов к YouTube API
'''

# from googleapiclient.discovery import build

# youtube = build('youtube', 'v3', credentials=credentials)

# Теперь вы можете использовать объект youtube для выполнения запросов к API
# В этом примере credentials представляет объект, содержащий токен доступа.

'''
Пример 2.
В приведенном ниже примере URL-адреса запрашивается автономный доступ ( access_type=offline ) к области, 
которая разрешает доступ для просмотра учетной записи YouTube пользователя. Он использует добавочную авторизацию, 
чтобы гарантировать, что новый токен доступа охватывает все области, к которым пользователь ранее предоставил доступ приложению. 
URL-адрес также устанавливает значения для обязательных параметров redirect_uri, response_type и client_id , 
а также для параметра state . URL-адрес содержит разрывы строк и пробелы для удобства чтения.

https://accounts.google.com/o/oauth2/v2/auth?
scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fyoutube.readonly&
include_granted_scopes=true&
state=state_parameter_passthrough_value&
redirect_uri=http%3A%2F%2Flocalhost%2Foauth2callback&
response_type=token&
client_id=client_id

'''

# 1. `https://accounts.google.com/o/oauth2/v2/auth`: Это базовый URL для инициации процесса аутентификации с 
# использованием OAuth 2.0 через Google.

# 2. `scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fyoutube.readonly`: Это параметр `scope`, 
# который указывает, к каким данным и функциональности вашему приложению нужен доступ. В данном случае, это область 
# (scope) `https://www.googleapis.com/auth/youtube.readonly`, что означает, что ваше приложение запрашивает доступ к чтению 
# данных YouTube в режиме "только для чтения".

# 3. `include_granted_scopes=true`: Этот параметр указывает, нужно ли включить в выданные разрешения 
# (scopes) их предоставившиеся разрешения. В данном случае, `true` означает, что включены.

# 4. `state=state_parameter_passthrough_value`: Этот параметр `state` используется для передачи произвольного значения, 
# которое будет возвращено приложению после успешной аутентификации. Это может использоваться для безопасной передачи информации 
# между приложением и сервером авторизации.

# 5. `redirect_uri=http%3A%2F%2Flocalhost%2Foauth2callback`: Этот параметр `redirect_uri` указывает на адрес, на который 
# будет перенаправлен пользователь после успешной аутентификации. В данном случае, это `http://localhost/oauth2callback`. 
# После аутентификации, токен доступа будет передан обратно на этот адрес.

# 6. `response_type=token`: Этот параметр `response_type` указывает тип ответа, который вы ожидаете. В данном случае, 
# это `token`, что означает, что вы ожидаете получить токен доступа без необходимости обмена кода авторизации на токен.

# 7. `client_id=client_id`: Этот параметр `client_id` представляет идентификатор вашего приложения (клиента), 
# который был предоставлен при регистрации приложения в Google API Console.

# Когда пользователь перейдет по этой URL-строке, он будет перенаправлен на страницу аутентификации Google, 
# где ему будет предложено предоставить доступ к запрошенным областям вашему приложению. После успешной аутентификации, 
# пользователь будет перенаправлен обратно на указанный `redirect_uri` с токеном доступа в URL-фрагменте.