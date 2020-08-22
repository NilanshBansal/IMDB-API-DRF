from django.db import models

class Movie(models.Model):
    popularity = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    director = models.CharField(max_length=200, blank=True)
    genre = models.TextField(null=True, blank=True)
    imdb_score = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
