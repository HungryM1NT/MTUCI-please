from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    level = models.IntegerField(default=1)
    first_level_score = models.IntegerField(default=0)
    second_level_score = models.IntegerField(default=0)
