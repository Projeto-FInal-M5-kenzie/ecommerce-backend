#Desenvolvido pela Consultoria Técnica da Gerencianet

import requests
import base64
from utils.credentials import credentials
import os
import dotenv

dotenv.load_dotenv()


credentials_user = {
    'client_id': credentials.CREDENTIALS['client_id'],
    "client_secret": credentials.CREDENTIALS['client_secret'],
}

certificate = credentials.CREDENTIALS['certificate']  # A variável certificado é o diretório em que seu certificado em formato .pem deve ser inserido

auth = base64.b64encode(
    (f"{credentials_user['client_id']}:{credentials_user['client_secret']}"
     ).encode()).decode()

url = "https://api-pix-h.gerencianet.com.br/oauth/token"  #Para ambiente de Desenvolvimento

payload="{\r\n    \"grant_type\": \"client_credentials\"\r\n}"
headers = {
    'Authorization': f"Basic {auth}",
    'Content-Type': 'application/json'
}

# requests.request("POST",
#                         url,
#                         headers=headers,
#                         data=payload,
#                         cert=certificate)

# print(response.text)