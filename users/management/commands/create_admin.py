from users.models import User
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    help = 'Create random users'

    def add_arguments(self, parser):

        parser.add_argument( '--username', '-u', type=str, help='Define a username prefix')
        parser.add_argument( '--password', '-p', type=str, help='Define a password prefix')
        parser.add_argument( '--email', '-e', type=str, help='Define a email prefix')

    def handle(self, *args, **kwargs):

        username = kwargs['username']
        password = kwargs['password']
        email = kwargs['email']

        if username : username = username 
        else: username = "admin"

        if email : email = email
        else: email = f'{username}@example.com'

        if password : password = password
        else: password = "admin1234"
        
        try:
            
            user_from_username = User.objects.filter(username=username)
            user_from_email = User.objects.filter(email=email)

            if len(user_from_username) > 0 or len(user_from_email) > 0:
            
                if len(user_from_username) > 0  and user_from_username[0].username == username :
                    raise CommandError( f'Username `{username}` already taken.' )

                if len(user_from_email) > 0 and user_from_email[0].email == email:
                    raise CommandError( f'Email `{email}` already taken.' )

            raise User.DoesNotExist('User not exist')

        except User.DoesNotExist:

            User.objects.create_superuser( username=username, password=password, email=email )

            self.stdout.write(self.style.SUCCESS(f"Admin `{username}` successfully created!"))