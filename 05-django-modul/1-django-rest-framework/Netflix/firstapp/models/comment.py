from django.db import models
from .movie import Movie
from django.contrib.auth.models import User


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.movie.name}"
