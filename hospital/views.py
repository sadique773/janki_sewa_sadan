from django.shortcuts import render
from .models import Doctor,Gallery


# Create your views here.

def home(request):
    doctors = Doctor.objects.all()
    photos = Gallery.objects.all()
    return render(request, "home.html", {"doctors": doctors,"photos": photos})