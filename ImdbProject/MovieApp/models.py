from django.db import models

# Create your models here.
    
class MovieData(models.Model):
    imdb_title_id = models.BigIntegerField(unique=True, null=True)
    original_title = models.CharField(max_length=250, null=True)
    year = models.CharField(max_length=4, null=True)
    date_published = models.DateField(null=True)
    genre = models.TextField(null=True)
    duration = models.BigIntegerField(null=True)
    language = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True)
    reviews_from_user = models.IntegerField(null=True,blank=True)
    reviews_from_critics = models.IntegerField(null=True,blank=True)