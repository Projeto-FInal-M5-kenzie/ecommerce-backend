from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from payments.models import PixModel


# Create your views here.
class TokenView(APIView):
    def post(self, req: Request) -> Response:
        pix_model = PixModel()

        response = pix_model.get_token()
        return Response(response)

class PixView(APIView):

    def post(self,request: Request)-> Response:
        payload = request.data
        txid = dict(txid=payload.pop('txid'))
        pix_model = PixModel()
        # pix_model.create_charge()
        response = pix_model.create_charge(txid=txid, payload=payload)

        return Response(response, status=response.status_code)