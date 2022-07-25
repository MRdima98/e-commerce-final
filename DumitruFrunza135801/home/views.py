from django.shortcuts import render

# Create your views here.

from hotel.models import Hotel

def home(request):
    return render(request, "index.html", {})

def search(request, city):
    result = Hotel.objects.filter(city = city) 
    context = {
        "result" : result
    }
    return render(request, "search.html", context)