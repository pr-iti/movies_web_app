from watchlist_app.models import WatchList,StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer,StreamSerializer
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.decorators import APIView


class StreamPlatformList(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamSerializer(platform , many = True,context={'request': request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StreamSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class StreamPlatformDetailAV(APIView):
    
    def get(self,request,pk):
        try:
            platform = StreamPlatform.objects.get(pk = pk)
        
            
        except platform.DoesNotExist:
            return Response({'error':'error found'},status = status.HTTP_404_NOT_FOUND)
        
        serializer = StreamSerializer(platform, context={'request': request})
        return Response(serializer.data,status = status.HTTP_200_OK)
        
        
    def put(self,request,pk):
        try:
            platform = StreamPlatform.objects.get(pk = pk)
        
            
        except platform.DoesNotExist:
            return Response({'error':'error found'},status = status.HTTP_404_NOT_FOUND)
        
        serializer = StreamSerializer(platform,data = request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status = status.HTTP_200_OK)
        else:
           return Response(serializer.errors)
        

    def delete(self,request,pk):
        try:
            platform = StreamPlatform.objects.get(pk = pk)
        
            
        except platform.DoesNotExist:
            return Response({'error':'error found'},status = status.HTTP_404_NOT_FOUND)
        
        platform.delete()
        
        return Response(status = status.HTTP_204_NO_CONTENT)
       
      

class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many = True,)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def post(self,request):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    
        
        
class WatchListDetailAV(APIView):
    
    def get(self,request,pk):
         try:
          movie = WatchList.objects.get(pk = pk)
         except WatchList.DoesNotExist:
            return Response({'error':'error found'},status = status.HTTP_404_NOT_FOUND)
        
         serializer = WatchListSerializer(movie)
         return Response(serializer.data,status = status.HTTP_200_OK)
        
    def put(self,request,pk):
        try:
          movie = WatchList.objects.get(pk = pk)
        except WatchList.DoesNotExist:
            return Response({'error':'error found'},status = status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(movie,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        
        
        
    def delete(self,request,pk):
        try:
          movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'error found'},status = status.HTTP_404_NOT_FOUND)
        
        movie.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
        
        
    
        
    
        
    
    
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True) # many=True for multiple dictionary dataset
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else :
#             return Response(serializer.errors)
            
         

# @api_view(['GET','DELETE','PATCH','PUT'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:
#           movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':'error found'},status = status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data,status = status.HTTP_200_OK)
    
#     if request.method == 'PUT':
#         try:
#           movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':'error found'},status = status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movie,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors)
        
#     if request.method == 'PATCH':
#         try:
#           movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':'error found'},status = status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({serializer.data},status = status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         try:
#           movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':'error found'},status = status.HTTP_404_NOT_FOUND)
        
#         movie.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
    