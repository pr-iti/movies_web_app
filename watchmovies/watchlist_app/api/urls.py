from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_detail
from watchlist_app.api.views import WatchListDetailAV,WatchList,StreamPlatformList

urlpatterns = [
    path('movie-list/',WatchList.as_view(),name = 'Watch-List'),
    path('movie/<int:pk>/',WatchListDetailAV.as_view(),name = 'WatchList-Detail'),
    path('stream/',StreamPlatformList.as_view(),name = 'Stream-platform-list')
   
#     path('movie-list/',movie_list,name = 'movie-list'),
#     path('movie/<int:pk>/',movie_detail,name = 'movie-detail')

]