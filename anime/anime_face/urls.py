from django.contrib import admin
from django.urls import path,include
from anime_face import views

urlpatterns =[
    path("",views.home,name="home" ),
]

from django.urls import path
from .views import login_view

urlpatterns = [
    path("", login_view, name="login"),
]