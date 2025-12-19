from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_detail
from watchlist_app.api.views import (WatchListDetailAV,WatchListAV,StreamPlatformList,       StreamPlatformDetailAV,                               ReviewList, ReviewCreate,                                    ReviewDetail)

urlpatterns = [
    path('movie-list/',WatchListAV.as_view(),name = 'Watch-List'),
    path('movie/<int:pk>/',WatchListDetailAV.as_view(),name = 'WatchList-Detail'),
    path('stream/',StreamPlatformList.as_view(),name = 'Stream-platform-list'),
    path('stream/<int:pk>/',StreamPlatformDetailAV.as_view(),name = 'Stream-platform-Detail'),
    
    
    # path('review/',ReviewList.as_view(),name='Review-List'),
    # path('review/<int:pk>/',ReviewDetail.as_view(),name='Review-Detail'),
    
    path('stream/<int:pk>/review-create/',ReviewCreate.as_view(),name = 'Review-Create'),
    path('stream/<int:pk>/review/',ReviewList.as_view(),name = 'Stream-platform-Detail'),
    path('stream/review/<int:pk>/',ReviewDetail.as_view(),name='Stream-Review-Detail')
   
#     path('movie-list/',movie_list,name = 'movie-list'),
#     path('movie/<int:pk>/',movie_detail,name = 'movie-detail')

]