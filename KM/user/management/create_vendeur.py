from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from user.models import Profil

class Command(BaseCommand):
    help = 'Crée un compte vendeur'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)

    def handle(self, *args, **options):
        User = get_user_model()
        username = options['username']
        email = options['email']
        password = options['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True
        )

        Profil.objects.create(user=user, user_type='vendeur')

        self.stdout.write(self.style.SUCCESS(f'Vendeur {username} créé avec succès'))