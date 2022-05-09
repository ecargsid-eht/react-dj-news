from django.urls import path
from .views import *


urlpatterns = [
    path("posts/",PostView.as_view(),name="posts"),
    path("category/",categoryView,name="category"),
    path("create-cat/",categoryCreate,name="postCreate"),
    path("create-post/",postCreate,name="postCreate"),
    path("login/",MyTokenObtainPairView.as_view(),name="login"),
]



