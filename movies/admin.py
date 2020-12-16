from django.contrib import admin
from .models import Participant, Movie, Category, Review, Genre, Country


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']     # зададим поля, которые можно редактировать на странице спиcка
    prepopulated_fields = {'url': ('name', )}   # автоматическое заполнение поле slug в админке


class ParticipantAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name', )}


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name', )}


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Review)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Country)
