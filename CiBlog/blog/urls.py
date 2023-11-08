from django.urls import path 
from . import views

urlpatterns = [
   path("", views.PostList.as_view(), name="index"),
   path("post/<postPk>", views.PostList.as_view(), name="post"),
]
