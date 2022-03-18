import csv
from django.db import models
from pathlib import Path
from movie_show.models import Movie, Ratings

Movie.objects.all().delete()
Ratings.objects.all().delete()

print("Table dropped successfully")
BASE_DIR = Path(__file__).resolve().parent.parent
data_link = str(BASE_DIR) + '/movei/data/movie.csv'

with open(data_link, encoding='latin-1') as file:
    reader = csv.reader(file, delimiter=",")
    next(reader)
    for row in reader:
        movie_obj = Movie.objects.create(
            title=row[2],
            poster=row[5],
            genre=row[4])
        rating_obj = Ratings.objects.create(
            movie=movie_obj,
            rating=float(row[3]),
            link=row[1]
        )

        movie_obj.save()
        rating_obj.save()
print("data parsed")
