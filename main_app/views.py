from django.shortcuts import render
from .models import Car

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_idx(request):
    cars = Car.objects.all()
    return render(request, 'cars/idx.html', {
        'cars': cars
    })