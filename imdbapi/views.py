from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import MovieSerializer
from .models import Movie
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User
import json

class MovieApiView(APIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = MovieSerializer
    def post(self, request, format=None):
        data = self.request.data
        for i in data:
            genre_modified = json.dumps(i['genre'])
            Movie.objects.get_or_create(popularity=i['99popularity'], director=i['director'], genre=genre_modified, imdb_score=i['imdb_score'], name=i['name'])
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PDMovieApiView(APIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = MovieSerializer
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response({"msg":"Successfully Deleted!"},status=status.HTTP_204_NO_CONTENT)

class ListMovieApiView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class UserCreateApiView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request, format=None):
        data = self.request.data
        User.objects.create_user(username=data['username'], password=data['password'])
        return Response({'status':'success', 'msg':'User successfully created'}, status = status.HTTP_201_CREATED)

class AdminCreateApiView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request, format=None):
        data = self.request.data
        User.objects.create_superuser(username=data['username'], password=data['password'])
        return Response({'status':'success', 'msg':'Admin User successfully created'}, status = status.HTTP_201_CREATED)

class SearchViewApi(APIView):
    serializer_class = MovieSerializer
    def post(self, request, format=None):
        queryset = Movie.objects.all()
        data = self.request.data
        try:
            queryset = queryset.filter(name__icontains=data['name'])
        except:
            pass
        try:
            queryset = queryset.filter(genre__icontains=data['genre'])
        except:
            pass
        try:
            queryset = queryset.filter(director__icontains=data['director'])
        except:
            pass
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

