# Generated by Django 4.1 on 2023-05-30 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_city_options_alter_event_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='dete_end',
            new_name='date_end',
        ),
    ]
