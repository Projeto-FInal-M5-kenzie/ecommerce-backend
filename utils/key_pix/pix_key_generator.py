from gerencianet import Gerencianet
from utils.credentials import credentials
from utils.token.token_generate import requests, url, headers, payload, certificate
import ipdb
response = requests.request("POST",
                        url,
                        headers=headers,
                        data=payload,
                        cert=certificate).json()
# response.json()
gn = Gerencianet(
    credentials.CREDENTIALS
)

body = {
    'calendario': {
        'expiracao': 3600
    },
    'devedor': {
        'cpf': '12345678909',
        'nome': 'Francisco da Silva'
    },
    'valor': {
        'original': '123.45'
    },
    'chave': '71cdf9ba-c695-4e3c-b010-abb521a3f1be',
    'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

key = gn.pix_create_evp()
# gn.
# headers["Authorization"] = f'{response["token_type"]} {response["access_token"]}'
# a=requests.request("POST",
#                        " https://api-pix-h.gerencianet.com.br/v2/gn/evp",
#                         headers=headers,
#                         # data=payload,
#                         cert=certificate).json()
# key =  gn.pix_create_immediate_charge(body=body)
ipdb.set_trace()
print(key)