from django.shortcuts import render,get_object_or_404
from .models import MovieData
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import MovieDataSerializer

def listAllMoviesOnTemplate(request):
    all_movies = MovieData.objects.all().order_by('id')
    return render(request,'MovieTable.html',{'all_movies':all_movies})

@api_view(['GET'])
def getMovieByGenre(request):
    for k,v in request.query_params.items():
        filter = k
        value = v
    if filter == 'genre':
        listOfMovies = []
        for obj in MovieData.objects.all():
            if value.capitalize() in obj.genre:
                listOfMovies.append(obj)
        retData = MovieDataSerializer(listOfMovies,many=True)
        return Response(retData.data, status=status.HTTP_202_ACCEPTED)
    elif filter == 'language':
        objlist = MovieData.objects.filter(language=value.capitalize())
        retData = MovieDataSerializer(objlist, many=True)
        return Response(retData.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({"message":"Invalid Query Params"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)