from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Movie, Genre


# class MoviesView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, "movies/movie_list.html", {"movie_list": movies})

class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)

# class MovieDetailView(View):
#     def get(self, request, movie_slug):
#         movie = Movie.objects.get(url=movie_slug)
#         return render(request, "movies/movie.html", {"movie": movie})


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"
    template_name = "movies/movie_detail.html"