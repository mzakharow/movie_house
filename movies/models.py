from django.db import models


class Category(models.Model):
    name = models.CharField('Категория', max_length=128)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Participant(models.Model):
    name = models.CharField('Имя', max_length=128)
    age = models.PositiveIntegerField('Возраст', default=0)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актеры и режиссеры'
        verbose_name_plural = 'Актеры и режиссеры'


class Genre(models.Model):
    name = models.CharField('Имя', max_length=128)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    title = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='movies/')
    year = models.PositiveIntegerField('Дата выхода', default=2020)
    country = models.CharField('Страна', max_length=32)
    director = models.ManyToManyField(Participant, verbose_name='режиссер', related_name='film_director')
    actors = models.ManyToManyField(Participant, verbose_name='актеры', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='жанры')

