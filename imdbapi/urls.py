from django.contrib import admin
from django.urls import path, include
from .views import MovieApiView, PDMovieApiView, ListMovieApiView, UserCreateApiView, AdminCreateApiView, SearchViewApi

urlpatterns = [
    path('movies/', MovieApiView.as_view()),
    path('putordelete/<int:pk>/', PDMovieApiView.as_view()),
    path('listmovies/', ListMovieApiView.as_view()),
    path('user/create/', UserCreateApiView.as_view()),
    path('admin/create/', AdminCreateApiView.as_view()),
    path('search/', SearchViewApi.as_view()),
]
