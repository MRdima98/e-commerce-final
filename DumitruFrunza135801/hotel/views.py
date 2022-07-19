from django.shortcuts import render
from django.http import HttpResponse

from .forms import RawHotelForm
from .models import Hotel

# Create your views here.
def hotel_view(request,*args,**kwargs):
    return render(request,"registra_struttura.html",{})

def struttura(request, *args, **kwargs):
    return render(request, "struttura.html",{})

def get_name(request):
    form = RawHotelForm()
    if request.method == 'POST':
        form = RawHotelForm(request.POST)
        if form.is_valid():
            Hotel.objects.create(**form.cleaned_data)
    else:
        form = RawHotelForm()
    return render(request, 'registra_struttura.html', {'form': form})