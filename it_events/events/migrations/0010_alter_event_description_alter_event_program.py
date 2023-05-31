# Generated by Django 4.1 on 2023-05-31 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_event_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Описание мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='program',
            field=models.TextField(max_length=3000, verbose_name='Программа мероприятия'),
        ),
    ]