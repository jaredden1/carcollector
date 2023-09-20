from django.shortcuts import render

cars = [
  {'make': 'Toyota', 'model': 'Supra', 'year': 1998},
  {'make': 'Genesis', 'model': 'Coupe 380GT', 'year': 2010},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_idx(request):
    return render(request, 'cars/idx.html', {
        'cars': cars
    })