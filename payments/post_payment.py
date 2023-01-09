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
    
#     curl -X POST \
#       'https://api.mercadopago.com/v1/payments' \
#       -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
#       -H 'Content-Type: application/json' \ 
#       -d '{
#   "additional_info": {
#     "items": [
#       {
#         "id": "MLB2907679857",
#         "title": "Point Mini",
#         "description": "Producto Point para cobros con tarjetas mediante bluetooth",
#         "picture_url": "https://http2.mlstatic.com/resources/frontend/statics/growth-sellers-landings/device-mlb-point-i_medium@2x.png",
#         "category_id": "electronics",
#         "quantity": 1,
#         "unit_price": 58.8
#       }
#     ],
#     "payer": {
#       "first_name": "Test",
#       "last_name": "Test",
#       "phone": {
#         "area_code": 11,
#         "number": "987654321"
#       },
#       "address": {}
#     },
#     "shipments": {
#       "receiver_address": {
#         "zip_code": "12312-123",
#         "state_name": "Rio de Janeiro",
#         "city_name": "Buzios",
#         "street_name": "Av das Nacoes Unidas",
#         "street_number": 3003
#       }
#     },
#     "barcode": {}
#   },
#   "description": "Payment for product",
#   "external_reference": "MP0001",
#   "installments": 1,
#   "metadata": {},
#   "payer": {
#     "entity_type": "individual",
#     "type": "customer",
#     "identification": {}
#   },
#   "payment_method_id": "visa",
#   "transaction_amount": 58.8
# }'