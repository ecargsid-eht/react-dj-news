from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Post
        fields = "__all__"
    
    # def create(self,validated_data):
    #     category = Category(**validated_data)
    #     category.save()
    #     Post(category = category)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = CategorySerializer(instance.category).data
        return response


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer,cls).get_token(user)
        token['username'] = user.username
        return token
