from rest_framework import serializers
from .models import Movie
import json

class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField()
    def get_genre(self, obj):
        jsonDec = json.decoder.JSONDecoder()
        genre_list = jsonDec.decode(obj.genre)
        return genre_list

    class Meta:
        model = Movie
        fields = '__all__'
        