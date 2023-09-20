from django.shortcuts import render

cars = [
  {'make': 'Toyota', 'model': 'Supra', 'year': 1998, 'description': 'The engine is rated at 321 horsepower and 315 lb-ft of torque. This allowed the MK4 Supra top speed to be 177 mph, but it was limited to 155 mph outside of Japan. The efficiency of sequential turbochargers allows the Mark 4 Supra to run 0-60 mph in 4.7 seconds.'},
  {'make': 'Genesis', 'model': 'Coupe 380GT', 'year': 2010, 'description': 'The engine now generates 348 horsepower at 6,400 rpm and 295 lb-ft of torque at 5,300 rpm. Thats 42 more horsepower than the previous generation and 11 percent more torque. With the extra power on hand, the Genesis Coupe 3.8 boasts a weight-to-power ratio of 10 pounds per horsepower.'},
  {'make': 'Acura', 'model': 'NSX', 'year': 1998, 'description': 'The standard engine on the NSX is an all-aluminum, 90-degree, 3.2-liter (3179 cc), dual-overhead-cam, 4-valve-per-cylinder V-6 which produces 290 horsepower at 7100 rpm and 224 lbs-ft of torque at 5500 rpm. It is mated to a 6-speed close-ratio manual transmission. Redline is at 8000 rpm.'},
  {'make': 'Mazda', 'model': 'RX 7', 'year': 1998, 'description': 'The engine in the second generation Mazda RX-7 was the same 13B rotary that had been introduced in 1984, but power output was raised to 146 hp, and an optional turbocharged model enjoyed 182 hp from the tiny 1.3-liter motor. The Turbo II, as it was called, also enjoyed larger front brakes.'},
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