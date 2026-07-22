from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import torch
import torchvision
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
import torch.nn as nn
from django.http import JsonResponse
import os
from django.conf import settings
import random
static_dir = settings.STATICFILES_DIRS[0]
class Generator(nn.Module):
  def __init__(self,noice_dimension=128):
    super().__init__()
    self.model= nn.Sequential(

        #Layer 1
        nn.ConvTranspose2d(
            in_channels=noice_dimension,
            out_channels =512,
            kernel_size=4,
            stride=1,
            padding=0,
            bias=False
        ),
        nn.BatchNorm2d(512),
        nn.ReLU(True),

        #Layer 2
        nn.ConvTranspose2d(
        in_channels=512,
        out_channels=256,
        kernel_size=4,
        stride=2,
        padding=1,
        bias=False
      ),

      nn.BatchNorm2d(256),

      nn.ReLU(True),

      #Layer 2
      nn.ConvTranspose2d(
        in_channels=256,
        out_channels=128,
        kernel_size=4,
        stride=2,
        padding=1,
        bias=False
      ),


      nn.BatchNorm2d(128),
      nn.ReLU(True),

        #layer 4
      nn.ConvTranspose2d(
      in_channels=128,
      out_channels=64,
      kernel_size=4,
      stride=2,
      padding=1,
      bias=False
      ),

      nn.BatchNorm2d(64),
      nn.ReLU(True),

        #layer 5
      nn.ConvTranspose2d(
      in_channels=64,
      out_channels=3,
      kernel_size=4,
      stride=2,
      padding=1,
      bias=False
      ),

      #Final layer use tanh since gan producec valu form -1 to 1
      nn.Tanh()
    )

  def forward(self,x):
        return self.model(x)
static_dir = settings.STATICFILES_DIRS[0]

os.makedirs(static_dir, exist_ok=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

generator = Generator().to(device)

checkpoint = torch.load(
        r"C:/Users/Administrator/Desktop/basna/anime/anime_face/gan_epoch_13_new.pth",
        map_location=device
    )

generator.load_state_dict(checkpoint["generator"])
generator.eval()



def generate_face_with_gan():

    with torch.no_grad():
        z = torch.randn(1, 128, 1, 1, device=device)
        fake = generator(z)

    pil_image = transforms.ToPILImage()(fake.squeeze(0).cpu())
    random_number = random.randint(1, 1000000)

    filename = f"generated_anime_face_{random_number}.png"

    save_path = os.path.join(static_dir, filename)

    pil_image.save(save_path)

    return f"/static/{filename}"




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