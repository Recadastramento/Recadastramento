import os
import pandas as pd
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Escopos de acesso
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Caminho para o arquivo de credenciais JSON
cod_token = "Projeto Recadastro\\Versão Deploy\\token.json"
cod_cred = "Projeto Recadastro\\Versão Deploy\\credentials.json"
CLIENT_SECRET_FILE = cod_token  # Altere para o seu caminho

# Verificar se o token de acesso já existe
if os.path.exists(cod_token):
    creds = Credentials.from_authorized_user_file(cod_token, SCOPES)
else:
    # Se não tiver, faça o login
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    creds = flow.run_local_server(port=0)

    # Salvar as credenciais para a próxima execução
    with open(cod_token, 'w') as token:
        token.write(creds.to_json())

# Construir o serviço
service = build('drive', 'v3', credentials=creds)

# ID do arquivo CSV no Google Drive
file_id = '1WtuPyPqtV0gZnnoPhLZLY1qfmgPNAv9vQDqK4NV6LQo'  # Substitua pelo ID do seu arquivo

# Baixar o arquivo CSV
request = service.files().export_media(fileId=file_id, mimeType='text/csv')
file = request.execute()

# Salvar o conteúdo em um arquivo
with open('arquivo.csv', 'wb') as f:
    f.write(file)

# Ler o arquivo CSV com pandas
df = pd.read_csv('arquivo.csv')
print(df)