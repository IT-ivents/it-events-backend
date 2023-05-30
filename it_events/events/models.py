from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Event(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='events', verbose_name='Автор публикации')
    title = models.CharField(
        "Название мероприятия", max_length=200, db_index=True)
    description = models.CharField(
        "Описание мероприятия", max_length=250)
    url = models.URLField(
        "Сайт мероприятия", max_length=200, unique=True)
    image = models.ImageField(
        verbose_name='Афиша мероприятия', upload_to='events/image',
        help_text='Загрузите фотографию')
    program = models.TextField(
        "Программа мероприятия", max_length=300)
    organizer = models.CharField(
        "Организатор", max_length=100)
    partners = models.CharField(
        "Партнеры", max_length=200, blank=True)
    address = models.CharField(
        "Адрес", max_length=200)
    price = models.DecimalField(
        "Цена", max_digits=8, decimal_places=2)
    date = models.DateTimeField(
        "Дата и время проведения")
    created_at = models.DateTimeField(
        "Дата создания записи", auto_now_add=True)
    # city = models.ManyToManyField(
    #     City, on_delete=models.CASCADE, verbose_name="Город проведения")
    # tags = models.ManyToManyField(
    #     Tags, on_delete=models.CASCADE, verbose_name="Теги")
    # professions = models.ManyToManyField(
    #     Profession, on_delete=models.CASCADE)
    # topik = models.ManyToManyField(
    #     Topic, on_delete=models.CASCADE, verbose_name="Направление")
    # format = models.ManyToManyField(
    #     Format, on_delete=models.CASCADE, verbose_name="Формат")


class City(models.Model):
    pass


class Tags(models.Model):
    pass


class Format(models.Model):
    pass


class Topic(models.Model):
    """Направление(Дизайн, Разработка)"""
    pass


class SubTopic(models.Model):
    """Под направление(Backend, Frontend)"""
    pass
