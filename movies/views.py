from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from rest_framework.viewsets import ModelViewSet

from .models import Movie, Genre, Category, Participant
from .forms import ReviewForm
from .serializer import MoviesSerializer


class Filters:
    @staticmethod
    def get_genres():
        return Genre.objects.all()

    @staticmethod
    def get_years():
        return Movie.objects.filter(draft=False).values("year")


# class MoviesView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, "movies/movie_list.html", {"movie_list": movies})


class MoviesView(Filters, ListView):
    paginate_by = 1
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


class MovieDetailView(Filters, DetailView):
    model = Movie
    slug_field = "url"  # по какому полю нужно искать запись
    # if there is no template_name, a template will be displayed <model_name> + '_detail' (there is movie_detail)
    # template_name = "movies/movie.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context


class MoviesListView(ModelViewSet):
    """DRF"""
    queryset = Movie.objects.filter(draft=False)
    serializer_class = MoviesSerializer


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


class FilterMoviesView(Filters, ListView):
    def get_queryset(self):
        year = self.request.GET.getlist("year")
        genre = self.request.GET.getlist("genre")
        q_filter = Q()
        if not year[0] == '':
            q_filter |= Q(year__in=year)
        if len(genre) > 0:
            q_filter |= Q(genres__in=genre)
        if q_filter is None:
            q_filter = Q(draft=False)

        queryset = Movie.objects.filter(q_filter).order_by('year')
        # queryset = Movie.objects.filter(q_filter).order_by('url').distinct('url')  # don't work with sqlite
        return queryset


def movies_app(request):
    return render(request, 'movies.html')
