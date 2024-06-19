from django.shortcuts import render, HttpResponse
from .models import flight
from .models import train
from .models import cruise

# Create your views here.
def home(request):
    flights=flight.objects.all()
    trains=train.objects.all()
    cruises=cruise.objects.all()
    return render(request, "index.html",{'flights': flights,'trains': trains,'cruises': cruises})