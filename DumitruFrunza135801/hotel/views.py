from gc import get_objects
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .forms import HotelForm, RawHotelForm, RoomForm
from .models import Hotel, Room

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
            hotel = Hotel.objects.create(**my_form.cleaned_data)
            return redirect('/hotel/rooms/' + str(hotel.id))
        else:
            print("Dati non validi")
    context = { "form" : my_form }
    return render(request, 'registra_struttura.html', context )

def room(request, id):
    my_form = RoomForm()
    hotel = Hotel.objects.get(id=id)
    if request.method =='POST':
        my_form = RoomForm(request.POST)
        if my_form.is_valid():
            Room.objects.create(**my_form.cleaned_data, hotel=hotel)
            return redirect('/hotel/list')
        else: 
            print("Data not valid!")
    rooms_count = range(int(hotel.rooms))
    context = { "form" : my_form, "rooms_count" : rooms_count }
    return render(request, 'rooms.html', context) 
