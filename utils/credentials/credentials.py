import os
import dotenv

dotenv.load_dotenv()


# Put your app credentials here
CREDENTIALS = {
    'client_id': os.getenv("CLIENT_ID_PRODUCTION"),
    # 'client_id': "Client_Id_b72bf72edd16591ce367b4154aa41192f2177c68",
    'client_secret': os.getenv("CLIENT_SECRET_PRODUCTION"),
    'sandbox':  bool(int(os.getenv("SANDBOX_PRODUCTION"))),
    'certificate': os.getenv("CERTIFICATE_PRODUCTION"),
}
print(CREDENTIALS)