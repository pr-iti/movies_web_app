# from django.shortcuts import render
# from watchlist_app.models import Movie
# # from django.utils import Response
# from django.http import JsonResponse

# def movie_list(request):
#     movies = Movie.objects.all()
#     # print(movies.values())
    
#     data = {'movies': list(movies.values())}
#     return JsonResponse(data)

# def movie_detail(request,pk):
    
#     movie = Movie.objects.get(pk = pk)
#     # convert the retrieved data to dictionary to show in json format
#     data = {
#         'name' : movie.name,
#         'description' : movie.description,
#         'active' : movie.active
#     }
    
#     return JsonResponse(data)
'''

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
'''


