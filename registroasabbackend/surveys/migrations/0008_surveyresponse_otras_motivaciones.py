# Generated by Django 5.0.6 on 2024-05-26 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0007_surveyresponse_municipio_aledano'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyresponse',
            name='otras_motivaciones',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
