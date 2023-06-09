# Generated by Django 4.1 on 2023-05-30 20:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Город проведения')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Формат')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='слаг')),
            ],
            options={
                'verbose_name': 'Формат',
                'verbose_name_plural': 'Форматы',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SubTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Направление')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='слаг')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Тэг')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='слаг')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Направление')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='слаг')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Название мероприятия')),
                ('description', models.CharField(max_length=250, verbose_name='Описание мероприятия')),
                ('url', models.URLField(unique=True, verbose_name='Сайт мероприятия')),
                ('image', models.ImageField(help_text='Загрузите фотографию', upload_to='events/image', verbose_name='Афиша мероприятия')),
                ('program', models.TextField(max_length=300, verbose_name='Программа мероприятия')),
                ('organizer', models.CharField(max_length=100, verbose_name='Организатор')),
                ('partners', models.CharField(blank=True, max_length=200, verbose_name='Партнеры')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Адрес')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('date', models.DateTimeField(verbose_name='Дата и время проведения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL, verbose_name='Автор публикации')),
            ],
        ),
    ]
