from django.conf import settings
from django.core.mail import send_mail
import random
import ipdb
# from .models import User

def send_account_activation_email(email, email_token):
    try:

        subject = "Your account needs to be verified"
        message = f"Click on the link to verify https://e-commerce-api-m0va.onrender.com/api/user/activate/{email_token}/"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            email,
        ]
        send_mail(subject, message, email_from, recipient_list)

    except Exception as error:
        return False
    return True


def send_otp_mail(email, otp):
    try:
        # user = User.objects.get(username=username)

        subject = "Your confirmation login"
        # otp = random.randint(1000, 9999)
        message = f'Your PIN is {otp}'
        email_from = settings.EMAIL_HOST_USER

        send_mail(subject, message, email_from, [email])
    except Exception as error:
        return False
    return True
