from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Movie, Genre, Category
from .forms import ReviewForm

# class MoviesView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, "movies/movie_list.html", {"movie_list": movies})


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # if if there is no tamplate name, a template will be displayed <model_name> + 'list'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context


# class MovieDetailView(View):
#     def get(self, request, movie_slug):
#         movie = Movie.objects.get(url=movie_slug)
#         return render(request, "movies/movie.html", {"movie": movie})


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"
    # if there is no tamplate_name, a template will be displayed <model_name> + '_detail' (here is movie_detail)
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
