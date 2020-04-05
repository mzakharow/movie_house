from django.urls import path

from . import views


urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name='movie_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review'),
    path("participant/<slug:slug>/", views.ParticipantView.as_view(), name='participant_detail'),
]
