# import requests

# def post_payment(payer_data):
#     url = "http://api.mercadopago.com/v1/payments?access_token=TEST-1456186532876383-010914-709b2f898ee6caf3cf3b95bc05996bbb-358726227"
#     payload = {
#         "transaction_amount": payer_data["transaction_amount"],
#         "token": payer_data["card_token"],
#         "description": payer_data["description"],
#         "installments": payer_data["installments"],
#         "payment_method_id": payer_data["payment_method_id"],
#         "payer":{
#             "email": "teste@test.com.br"
#         }
#     }

#     header = {"x-meli-session": payer_data["deviceId"]}
    
#     response = requests.post(url=url, json=payload, headers=header)

#     if requests.status_codes == 200 or requests.status_codes == 201:
#         print("SUcesso")
    
#     print("merda")
    
#     