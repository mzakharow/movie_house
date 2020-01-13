from django.contrib import admin
from .models import Participant, Movie, Category, Rating, RatingStar, Review, Genre, Country


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']     # зададим поля, которые можно редактировать на странице спиcка
    prepopulated_fields = {'url': ('name', )}   # автоматическое заполнение поле slug в админке


admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie)
admin.site.register(Participant)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(Country)
