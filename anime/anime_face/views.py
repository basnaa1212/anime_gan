from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.http import JsonResponse



# Create your views here.
def home(request):

    return render(request,"anime_face/home.html")



def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "anime_face/login.html")


def home1(request):
    return render(request, 'anime_face/home_page.html')


def generate_anime(request):

    # Call GAN model here
    image_path = generate_face_with_gan()

    return JsonResponse({
        "image_url": image_path
    })