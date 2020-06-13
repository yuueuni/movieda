from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from ..movies.models import Actor, Director, Movie

# Create your models here.
class User(AbstractUser):
    birthday = models.DateTimeField(null=True)
    gender = models.BooleanField(default=True)
    favorite_actors = models.ManyToManyField(Actor, null=True, blank=True, related_name='user_favor')
    favorite_directors = models.ManyToManyField(Director, null=True, blank=True, related_name='user_favor')
    favorite_movies = models.ManyToManyField(Movie, null=True, blank=True, related_name='user_favor')