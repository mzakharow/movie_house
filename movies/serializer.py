from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer, ListSerializer

from movies.models import Movie, Participant


class ParticipantsSerializer(ModelSerializer):
    class Meta:
        model = Participant
        fields = ['name', 'age']


class MoviesSerializer(ModelSerializer):
    # country = SlugRelatedField(many=True, read_only=True, slug_field='title')
    country = ListSerializer(child=serializers.CharField())
    genres = ListSerializer(child=serializers.CharField())
    # actors = serializers.StringRelatedField(many=True)
    actors = ParticipantsSerializer(many=True, read_only=True)
    # director = ListSerializer(child=serializers.CharField())
    director = ParticipantsSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['title', 'year', 'country', 'actors', 'director', 'genres', 'poster', 'description', 'url']
