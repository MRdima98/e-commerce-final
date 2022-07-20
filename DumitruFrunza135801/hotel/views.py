from multiprocessing import context
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
    my_form = RawHotelForm()
    if request.method == 'POST':
        my_form = RawHotelForm(request.POST)
        if my_form.is_valid():
            Hotel.objects.create(**my_form.cleaned_data)
        else:
            print("Dati non validi")
    context = { "form" : my_form }
    return render(request, 'registra_struttura.html', context )