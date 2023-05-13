from rest_framework.serializers import ModelSerializer
from .models import MovieData

class MovieDataSerializer(ModelSerializer):
    class Meta:
        model = MovieData
        exclude = ('id',)