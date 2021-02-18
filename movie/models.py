from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=512)
    overal_rate = models.IntegerField(max_length=1, default=0)


class Rate(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.IntegerField(max_length=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
