from rest_framework import serializers
from django.db import models

from watchlist_app.models import WatchList,StreamPlatform, Review

class ReviewListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model= Review
        fields = '__all__' #['id','name','description','active']
        # exclude =['active']
     
     
class WatchListSerializer(serializers.ModelSerializer):
    
    reviews = ReviewListSerializer(many = True)
    #adds a len_name field to the models and objects
    len_name = serializers.SerializerMethodField()
    # StreamPlatform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE)
    class Meta:
        model= WatchList
        fields = '__all__'
        
        # exclude =['active']
        
    def get_len_name(self, object):
        return len(object.title)
    

class StreamSerializer(serializers.HyperlinkedModelSerializer):
    #adds a len_name field to the models and objects
    
    #adds the relation b/t streaming & movie list
    # watchlist = WatchListSerializer(many = True,read_only=True)
    
    # custom field in the serializer to display for relations
    # watchlist = serializers.StringRelatedField(many = True,read_only=True)
    
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='WatchList-Detail'
    )
    len_name = serializers.SerializerMethodField()
    class Meta:
        model= StreamPlatform
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'Stream-platform-Detail', 'lookup_field': 'pk'}
        }
        
    def get_len_name(self, object):
        return len(object.name) 
        
        
        
        

     
    # def validate(self,data):
    #     if data["name"] == data["description"]:
    #         raise serializers.ValidationError("name and decpn, can't be same")
    #     else:
    #         return data  

    # def length_check(self,value):
    #     if len(value) < 2 :
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
    

# class MovieSerializer(serializers.Serializer):
#     id = serializers.CharField()
#     name = serializers.CharField(validators =[length_check])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
        
#         instance.name = validated_data.get("name",instance.name)
#         instance.description = validated_data.get("description",instance.description)
#         instance.active = validated_data.get("active",instance.active)
#         instance.save()
        
#         return instance
    
#     def validate(self,data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("name and decpn, can't be same")
#         else:
#             return data   
        
    
       
    # def validate_name(self, value):
        
    #     if len(value) < 2 :
    #         raise serializers.ValidationError("Name is too short")
    #     else:
            
    #        return value