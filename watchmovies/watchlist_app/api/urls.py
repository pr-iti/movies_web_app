from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_detail
from watchlist_app.api.views import MovieListAV,MovieDetailAV

urlpatterns = [
    path('movie-list/',MovieListAV.as_view(),name = 'movie-list'),
    path('movie/<int:pk>/',MovieDetailAV.as_view(),name = 'movie-detail')
   
#     path('movie-list/',movie_list,name = 'movie-list'),
#     path('movie/<int:pk>/',movie_detail,name = 'movie-detail')

]