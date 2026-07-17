from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,"anime_face/home.html")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

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