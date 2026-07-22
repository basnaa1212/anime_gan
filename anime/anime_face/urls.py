from django.contrib import admin
from django.urls import path,include
from anime_face import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path(
        "",
        auth_views.LoginView.as_view(template_name="anime_face/login.html"),
        name="login",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),
    path("home/", views.home1, name='home'),
    path('generate/', views.generate_anime, name='generate'),
]