from django.contrib.auth import get_user_model
from rest_framework import serializers

from movies.serializers import MovieSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    favorite_movies = MovieSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'favorite_movies', )
