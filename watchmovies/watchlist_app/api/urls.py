from django.urls import path,include
from watchlist_app.api.views import movie_list,movie_detail

urlpatterns = [
   
    path('movie-list/',movie_list,name = 'movie-list'),
    path('movie/<int:pk>/',movie_detail,name = 'movie-detail')
]