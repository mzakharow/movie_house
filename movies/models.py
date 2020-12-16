import xml.etree.ElementTree as ET
import requests
from xml.etree import ElementTree
from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField


def image_folder(instance, filename):
    filename = instance.url + '.' + filename.split('.')[1]    # filename.split('.')[1]- расширение файла
    return f'{instance._meta.model_name}/{instance.url}/{filename}'


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
    image = models.ImageField('Изображение', upload_to=image_folder)
    url = models.SlugField(max_length=128, unique=True)

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


class Country(models.Model):
    title = models.CharField('Название', max_length=64, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Movie(models.Model):
    title = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to=image_folder)
    year = models.PositiveIntegerField('Дата выхода', default=2020)
    country = models.ManyToManyField(Country, verbose_name='страна', related_name='film_country')
    director = models.ManyToManyField(Participant, verbose_name='режиссер', related_name='film_director')
    actors = models.ManyToManyField(Participant, verbose_name='актеры', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='жанры')
    budget = models.PositiveIntegerField('Бюджет', default=0, help_text='в долларах')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=128, unique=True)
    video = EmbedVideoField(blank=True, verbose_name='Видео')
    kinopoisk = models.CharField('ID_Kinopoisk', default='0', max_length=8)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    @property
    def get_rating(self):
        rating = {'kinopoisk': 'n/a', 'imdb': 'n/a'}
        response = requests.get(f'https://rating.kinopoisk.ru/{self.kinopoisk}.xml')
        tree = ElementTree.fromstring(response.content)
        for attr in tree:
            if attr.tag == 'kp_rating':
                rating['kinopoisk'] = attr.text
            elif attr.tag == 'imdb_rating':
                rating['imdb'] = attr.text
        return rating

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=64)
    text = models.TextField('Отзыв', max_length=3072)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

