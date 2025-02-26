# This module helps create a superuser command

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    help = 'Creates a superuser non-interactively if it does not exist'

    def handle(self, *args, **options):
        username = os.environ.get('SUPERUSER_USERNAME')
        password = os.environ.get('SUPERUSER_PASSWORD')
        email = os.environ.get('SUPERUSER_EMAIL', '')

        if not username or not password:
            self.stdout.write(self.style.ERROR(
                "SUPERUSER_USERNAME and SUPERUSER_PASSWORD environment \
variables must be set"))
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(
                f'Superuser {username} created successfully.'
            ))
        else:
            self.stdout.write(self.style.WARNING(
                f'Superuser {username} already exists.'
            ))

