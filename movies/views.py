from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Movie, Genre, Category, Participant
from .forms import ReviewForm


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


# class MoviesView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, "movies/movie_list.html", {"movie_list": movies})


class MoviesView(GenreYear, ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # if there is no tamplate name, a template will be displayed <model_name> + 'list'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context


# class MovieDetailView(View):
#     def get(self, request, movie_slug):
#         movie = Movie.objects.get(url=movie_slug)
#         return render(request, "movies/movie.html", {"movie": movie})


class MovieDetailView(GenreYear, DetailView):
    model = Movie
    slug_field = "url"  # по какому полю нужно искать запись
    # if there is no template_name, a template will be displayed <model_name> + '_detail' (there is movie_detail)
    # template_name = "movies/movie.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            # form.movie_id = pk  # turn refer to related field
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ParticipantView(DetailView):
    model = Participant
    # template_name = 'movies/participant_detail.html'
    slug_field = 'url'  # field for search


class FilterMoviesView(GenreYear, ListView):
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |    # Q как логическое ИЛИ
            Q(genres__in=self.request.GET.getlist("genre"))   # , как просто И
        )
        return queryset
