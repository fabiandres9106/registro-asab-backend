# Generated by Django 5.0.6 on 2024-06-02 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_rename_attended_ticket_check_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='reserver_tickets',
        ),
    ]
