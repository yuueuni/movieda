from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movies.models import Actor, Director, Movie

# Create your models here.
class User(AbstractUser):
    favorite_actors = models.ManyToManyField(Actor, blank=True, related_name='users')
    favorite_directors = models.ManyToManyField(Director, blank=True, related_name='users')
    favorite_movies = models.ManyToManyField(Movie, blank=True, related_name='users')