from django.core.mail import send_mail
import random
from django.conf import settings
from users.models import User

def send_otp_mail(email):
    subject = "Your confirmation login"
    otp = random.randint(1000, 9999)
    message = f'Your PIN is {otp}'
    email_from = settings.EMAIL_HOST

    send_mail(subject, message, email_from, [email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
