from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Create default users and assign them to groups'

    def handle(self, *args, **kwargs):
        users = [
            {'username': 'logistica', 'password': 'logistica.123', 'group': 'attendant'},
            {'username': 'produccion', 'password': 'produccion.123', 'group': 'producer'},
            {'username': 'admin_user', 'password': 'admin.123', 'group': 'admin'},
        ]

        for user_data in users:
            user, created = User.objects.get_or_create(username=user_data['username'])
            if created:
                user.set_password(user_data['password'])
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully created user {user.username}'))
            else:
                self.stdout.write(self.style.WARNING(f'User {user.username} already exists'))

            group, _ = Group.objects.get_or_create(name=user_data['group'])
            user.groups.add(group)
            self.stdout.write(self.style.SUCCESS(f'Added user {user.username} to group {group.name}'))