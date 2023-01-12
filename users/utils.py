from django.conf import settings
from django.core.mail import send_mail

def send_account_activation_email(email, email_token):
    try:
                
        subject = 'Your account needs to be verified'
        message = f'Click on the link to verify http://127.0.0.1:8000/api/users/activate/{email_token}/'
        email_from = settings.EMAIL_HOST_USER
        print(email_from)
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        
    except Exception as error:
        return False
    return True