from gerencianet import Gerencianet
from utils.credentials import credentials
from utils.key_pix.pix_key_generator import key
gn = Gerencianet(credentials.CREDENTIALS)

headers = {
    'x-skip-mtls-checking': 'false'
}

params = {
    'chave': key
}

body = {
    'webhookUrl': 'chain-pix-prod.crt'
}

response =  gn.pix_config_webhook(params=params, body=body, headers=headers)
print(response)