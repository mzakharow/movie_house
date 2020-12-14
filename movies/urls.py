from django.urls import path, re_path, include
from rest_framework.routers import SimpleRouter

from . import views
from .views import MoviesListView, movies_app

router = SimpleRouter()

router.register('api/movies', MoviesListView)

urlpatterns = [
    path("", views.MoviesView.as_view(), name='main'),
    path('captcha/', include('captcha.urls')),
    path("movies/", movies_app, name='movies'),  # vue.js
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name='movie_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review'),
    path("participant/<slug:slug>/", views.ParticipantView.as_view(), name='participant_detail'),
]

urlpatterns += router.urls
