from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    birthday = models.DateTimeField(null=True)
    gender = models.BooleanField(default=True)