# Generated by Django 5.0.6 on 2024-05-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0006_surveyresponse_comprension_datos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyresponse',
            name='municipio_aledano',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]