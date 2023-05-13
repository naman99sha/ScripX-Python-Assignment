from django.db import models

# Create your models here.
class Genre(models.Model):
    genreName = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return self.genreName
    
class MovieData(models.Model):
    imdb_title_id = models.BigIntegerField(unique=True, null=True)
    original_title = models.CharField(max_length=250, null=True)
    year = models.CharField(max_length=4, null=True)
    date_published = models.DateField(null=True)
    genre = models.ManyToManyField(Genre, related_name='MovieData_genre')
    language = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True)
    reviews_from_user = models.IntegerField(null=True)
    reviews_from_critics = models.IntegerField(null=True)