# Generated by Django 4.1 on 2023-07-09 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileEvent',
        ),
    ]