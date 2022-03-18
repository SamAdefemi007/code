from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    poster = models.URLField(
        max_length=500, default="https://unsplash.com/photos/ZnLprInKM7s")
    genre = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Ratings(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0, blank=True, null=True)
    link = models.URLField(max_length=1000)

    def ___str__(self):
        return self.ratings
