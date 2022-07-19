from django import forms

from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta: 
         model = Hotel 
         fields = [
            'name',
            'IVA',
            'street',
            'stars',
            'cost',
            'rooms'
         ]


class RawHotelForm(forms.Form):
    name = forms.CharField(label='Nome' , max_length =50, widget=forms.TextInput(attrs={'class': 'form-control base-height','placeholder':'Nome albergo'}), help_text='Yes')
    IVA = forms.CharField(label=None , max_length =15, widget=forms.TextInput(attrs={'class': 'form-control base-height','placeholder':'IVA'}), help_text='Yes')
    street = forms.CharField(label=None , max_length =50, widget=forms.TextInput(attrs={'class': 'form-control base-height very-light-top-margin','placeholder':'Via'}), help_text='Yes')
    stars = forms.CharField(label=None , widget=forms.TextInput(attrs={'class': 'form-control base-height very-light-top-margin','placeholder':'Quante stelle'}), help_text='Yes')
    cost = forms.CharField(label=None , widget=forms.TextInput(attrs={'class': 'form-control base-height very-light-top-margin','placeholder':'Costo camera'}), help_text='Yes')
    rooms = forms.CharField(label=None , widget=forms.TextInput(attrs={'class': 'form-control base-height very-light-top-margin','placeholder':'Camere totali'}), help_text='Yes')
    my_hidden = forms.CharField(widget=forms.HiddenInput())
    #piscina = forms.BooleanField(label='Piscina', label_suffix='', required=False)
    #idro = forms.BooleanField(label='Idro', label_suffix='', required=False)
    #palestra = forms.BooleanField(label='Palestra', label_suffix='', required=False)
    #descrizione = forms.CharField(label=None, widget=forms.Textarea(attrs={'class': 'form-control light-top-margin no-resize','placeholder':'Descrizione'}), help_text='No')