from django.db import models
from django.urls import reverse


class GameGenre(models.Model):
    genre_name = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_name


class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    source_link = models.URLField(max_length=500)
    play_link = models.URLField(max_length=500, blank=True)
    genre = models.ManyToManyField(GameGenre)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('games:game-detail', args=[str(self.id)])
