from django.shortcuts import render
from .models import MovieData, Genre

def listAllMoviesOnTemplate(request):
    all_movies = MovieData.objects.all().order_by('id')
    return render(request,'MovieTable.html',{'all_movies':all_movies})
