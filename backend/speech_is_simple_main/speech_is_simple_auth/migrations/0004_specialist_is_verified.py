# Generated by Django 5.0.4 on 2024-05-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech_is_simple_auth', '0003_remove_user_username_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]
