from gc import get_objects
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404

from .forms import HotelForm, RawHotelForm
from .models import Hotel

# Create your views here.
def hotel_view(request,*args,**kwargs):
    return render(request,"registra_struttura.html",{})

def struttura(request, id):
    try:
        obj = Hotel.objects.get(id=id)
    except Hotel.DoesNotExist:
        raise Http404
    form = HotelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/hotel/list')
    context = {
        "form": form
    }
    return render(request, "registra_struttura.html", context)

def hotel_list(request):
    obj = Hotel.objects.all()
    context = { "objects": obj }
    return render(request, "hotel_list.html", context)

def delete_hotel(request, id):
    hotel = Hotel.objects.get(id=id)
    hotel.delete()
    return redirect('/hotel/list')

def new_hotel(request):
    my_form = RawHotelForm()
    if request.method == 'POST':
        my_form = RawHotelForm(request.POST)
        if my_form.is_valid():
            Hotel.objects.create(**my_form.cleaned_data)
            return redirect('/hotel/list')
        else:
            print("Dati non validi")
    context = { "form" : my_form }
    return render(request, 'registra_struttura.html', context )