from django.contrib import admin
from django.urls import path,include
from anime_face import views

urlpatterns =[
    path("", views.login_view, name="login"),
    path("home/", views.home1, name='home'),
    path('generate/', views.generate_anime, name='generate'),
]