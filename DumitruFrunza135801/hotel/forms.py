from datetime import date
from pickletools import decimalnl_long
from django import forms

from .models import Hotel, Room

class HotelForm(forms.ModelForm):
    name = forms.CharField(label=None , max_length =50, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control base-height',
                'placeholder':'Nome albergo'}), help_text='Yes')
    IVA = forms.CharField(label=None , max_length =15,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control base-height',
                'placeholder':'IVA'}), help_text='Yes')
    street = forms.CharField(label=None , max_length =50, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control base-height very-light-top-margin',
                'placeholder':'Via'}), help_text='Yes')
    CAP = forms.DecimalField(label=None , 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control base-height very-light-top-margin',
                'placeholder':'CAP'}), help_text='Yes')
    city = forms.CharField(label=None , max_length =50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control base-height very-light-top-margin',
                'placeholder':'Città'}), help_text='Yes')
    stars = forms.DecimalField(label=None , 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control base-height very-light-top-margin',
                'placeholder':'Quante stelle'}), help_text='Yes')
    rooms = forms.DecimalField(label=None, widget=forms.TextInput(
            attrs={
                'class': 'form-control base-height very-light-top-margin',
                'placeholder':'Camere totali'}), help_text='Yes')
    free_time = forms.CharField(label=None, widget=forms.Textarea(
            attrs={
                'class': 'form-control light-top-margin no-resize',
                'placeholder':'Elencare tutti i possbili passatempo e'
                'attività di svago'}), help_text='Svaghi')

    class Meta: 
         model = Hotel 
         fields = [
            'name',
            'IVA',
            'street',
            'CAP',
            'city',
            'stars',
            'rooms',
            'free_time',
         ]


class RawHotelForm(HotelForm):
    pass


class RoomForm(forms.Form):
    my_attrs = {'class': 'form-control base-height'}
    date_attrs = my_attrs.copy()
    date_attrs['type']='date'
    name = forms.CharField(label=None , max_length =50, 
        widget=forms.TextInput(my_attrs))
    start_period = forms.DateField(label=None, help_text="start",
        widget=forms.TextInput(date_attrs))
    stop_period = forms.DateField(label=None, help_text="stop",
        widget=forms.TextInput(date_attrs))
    start_period2 = forms.DateField(label=None, help_text="start2",
        widget=forms.TextInput(date_attrs))
    stop_period2 = forms.DateField(label=None, help_text="stop2",
        widget=forms.TextInput(date_attrs))
    start_period3 = forms.DateField(label=None, help_text="start3",
        widget=forms.TextInput(date_attrs))
    stop_period3 = forms.DateField(label=None, help_text="stop3",
        widget=forms.TextInput(date_attrs))
    cost = forms.DecimalField(label=None, help_text="cost",
        widget=forms.TextInput(my_attrs))

    class Meta: 
        model = Room
        fields = [
            'name',
            'start_period',
            'stop_period'
            'start_period2',
            'stop_period2'
            'start_period3',
            'stop_period3',
            'cost'
        ]
