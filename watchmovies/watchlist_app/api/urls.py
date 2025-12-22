from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from watchlist_app.api.views import movie_list,movie_detail
from watchlist_app.api.views import (WatchListDetailAV,WatchListAV,StreamPlatformList,StreamPlatformDetailAV,ReviewList,  ReviewCreate, ReviewDetail,ExampleView)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
    ),
    public=True,
)



urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),
    # JWT Authentication endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('movie-list/',WatchListAV.as_view(),name = 'Watch-List'),
    path('movie/<int:pk>/',WatchListDetailAV.as_view(),name = 'WatchList-Detail'),
    path('stream/',StreamPlatformList.as_view(),name = 'Stream-platform-list'),
    path('stream/<int:pk>/',StreamPlatformDetailAV.as_view(),name = 'Stream-platform-Detail'),
    path('api-token-auth/', ExampleView.as_view(), name= 'api-token'),
    
    path('review/',ReviewList.as_view(),name='Review-List-All'),
    path('review/<int:pk>/',ReviewDetail.as_view(),name='Review-Detail'),
    
    path('stream/<int:pk>/review-create/',ReviewCreate.as_view(),name = 'Review-Create'),
    path('stream/<int:pk>/review/',ReviewList.as_view(),name = 'Stream-platform-Detail'),
    path('stream/review/<int:pk>/',ReviewDetail.as_view(),name='Stream-Review-Detail')
   
#     path('movie-list/',movie_list,name = 'movie-list'),
#     path('movie/<int:pk>/',movie_detail,name = 'movie-detail')

]