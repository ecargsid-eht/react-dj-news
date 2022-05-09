from os import stat
from urllib import response
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
# Create your views here.


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(["GET"])
def categoryView(r):
    category = Category.objects.all()
    serializer = CategorySerializer(category,many = True)
    return Response(serializer.data)
    

@api_view(["POST"])
def categoryCreate(r):
    serializer = CategorySerializer(data=r.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def postCreate(r):
    serializer = PostSerializer(data=r.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    # return Response(serializer.data)

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer