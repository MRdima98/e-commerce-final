from django import forms

class NameForm(forms.Form):
    NomeAlbergo = forms.CharField(label='' , max_length =50, widget=forms.TextInput(attrs={'class': 'form-control base-height','placeholder':'Nome albergo'}))
    IVA = forms.CharField(label='' , max_length =15, widget=forms.TextInput(attrs={'class': 'form-control base-height','placeholder':'IVA'}))
    via = forms.CharField(label='' , max_length =50, widget=forms.TextInput(attrs={'class': 'form-control base-height very-light-top-margin','placeholder':'Via'}))
    stelle = forms.CharField(label='' , widget=forms.TextInput(attrs={'class': 'form-control base-height very-light-top-margin','placeholder':'Quante stelle'}))
    costoCamera = forms.CharField(label='' , widget=forms.TextInput(attrs={'class': 'form-control base-height very-light-top-margin','placeholder':'Costo camera'}))
    camereTot = forms.CharField(label='' , widget=forms.TextInput(attrs={'class': 'form-control base-height very-light-top-margin','placeholder':'Camere totali'}))
    piscina = forms.BooleanField(label='Opzioni')
    
    