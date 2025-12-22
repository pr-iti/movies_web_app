from watchlist_app.models import WatchList,StreamPlatform,Review
from watchlist_app.api.serializers import WatchListSerializer,StreamSerializer,ReviewListSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly 
# from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework import generics
from watchlist_app.api import permission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from watchlist_app.api.throttling import ReviewCreateThrottle, ReviewListThrottle

#-------------------------------------------------------------------------//
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Token creation moved to signals - don't create at module level
    
    
    
class ExampleView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # JWT Token
        }
        return Response(content)

# from rest_framework import mixins

class ReviewCreate(generics.CreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [ReviewCreateThrottle]
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movies =WatchList.objects.get(pk=pk)
        serializer.save(WatchList=movies)
        
        return super().perform_create(serializer)
    
# class ReviewListAll(generics.ListAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewListSerializer

class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [ReviewListThrottle]
    
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(WatchList = pk)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    permission_classes = [permission.AdminOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]



# class ReviewDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewListSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)




# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewListSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
    


class StreamPlatformList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
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
    permission_classes = [IsAuthenticatedOrReadOnly]
    
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
    permission_classes = [IsAuthenticatedOrReadOnly]
    
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
    permission_classes = [IsAuthenticatedOrReadOnly]
    
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
    