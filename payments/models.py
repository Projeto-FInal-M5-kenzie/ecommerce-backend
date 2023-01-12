from django.db import models
import base64
import requests
import os
import dotenv
import json
import pyqrcode
from utils.credentials import credentials
import ipdb
# from PIL import Image
from gerencianet import Gerencianet
from utils.credentials import credentials
import base64
from io import BytesIO

dotenv.load_dotenv()


class PaymentsOptions(models.TextChoices):
    PIX = "Pix"
    CARD = "Card"
    DEFAULT = "Not informed"


class Payment(models.Model):
    method_payment = models.CharField(
        max_length=30,
        choices=PaymentsOptions.choices,
        default=PaymentsOptions.DEFAULT,
    )
    total_price = models.FloatField()
    done = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    client = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="payments",
    )


class PixModel:
    def __init__(self):
        self.headers = {
            "Authorization": f'Bearer {self.get_token()}',
            'Content-Type': 'application/json'
        }
        self.url = os.getenv("URL_PRODUCTION")  # Para ambiente de Desenvolvimento
        self.certificate = credentials.CREDENTIALS["certificate"] 


    def get_token(
        self,
    ):
        url = os.getenv("URL_PRODUCTION")  # Para ambiente de Desenvolvimento
        certificate = credentials.CREDENTIALS["certificate"] 

        credentials_user = {
            "client_id": credentials.CREDENTIALS["client_id"],
            "client_secret": credentials.CREDENTIALS["client_secret"],
        }

        auth = base64.b64encode(
            (
                f"{credentials_user['client_id']}:{credentials_user['client_secret']}"
            ).encode()
        ).decode()

        headers = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}
        payload = {"grant_type": "client_credentials"}
        # ipdb.set_trace()

        response = requests.request(
            "POST", f'{url}/oauth/token', headers=headers, data=json.dumps(payload), cert=certificate
        )

        return json.loads(response.content)["access_token"]

    def create_qrcode(self, location_id):
        url = os.getenv("URL_PRODUCTION")  # Para ambiente de Desenvolvimento

        certificate = credentials.CREDENTIALS["certificate"] 
        response = requests.get(f'{url}/v2/loc/{location_id}/qrcode', headers=self.headers, cert=certificate)

        return json.loads(response.content)

    
    def create_order(self, txid, payload):
        gn = Gerencianet(credentials.CREDENTIALS)
        url = os.getenv("URL_PRODUCTION")  # Para ambiente de Desenvolvimento

        certificate = credentials.CREDENTIALS["certificate"] 
       
        headers = {
            "Authorization": f'Bearer {self.get_token()}',
            'Content-Type': 'application/json'
        }
        ipdb.set_trace()
        response = requests.put(f'{url}/v2/cob/{txid}', data=json.dumps(payload), headers=headers, cert=certificate)
        # response =  gn.pix_create_charge(params=txid,body=payload)

        if response.status_code == 201:
            return json.loads(response.content)
        
        return json.loads(response.content)

    
    def qrcode_generator(self, location_id):
        # qrcode = self.create_qrcode(location_id=location_id)

        # data_qrcode = qrcode['qrcode']

        # url = pyqrcode.QRCode(data_qrcode, error='H')
        # url.png("qrcode.png", scale=10)

        # img = Image.open("qrcode.png")
        # img = img.convert('RGBA')
        # img_io = BytesIO()
        # img.save(img_io, "PNG", quality=100)
        # img_io.seek(0)
        gn = Gerencianet(credentials.CREDENTIALS)

        params = {
            'id': location_id
        }

        response =  gn.pix_generate_QRCode(params=params)

        if('imagemQrcode' in response):
            with open("qrCodeImage.png", "wb") as fh:
                fh.write(base64.b64decode(response['imagemQrcode'].replace('data:image/png;base64,', '')))

    def create_charge(self, txid, payload):
        location_id = self.create_order(txid=txid, payload=payload).get('loc').get("id")
        qrcode = self.qrcode_generator(location_id=location_id)


        return qrcode