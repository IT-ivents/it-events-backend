# Generated by Django 4.1 on 2023-07-07 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_userevent_remove_userprofileevent_event_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileevent',
            name='event',
        ),
        migrations.RemoveField(
            model_name='userprofileevent',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='UserProfileEvent',
        ),
    ]