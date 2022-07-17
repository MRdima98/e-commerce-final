from django import forms

class NameForm(forms.Form):
    NomeAlbergo = forms.CharField(label='Nome' , max_length =50, widget=forms.TextInput(attrs={'class': 'form-control base-height','placeholder':'Nome albergo'}), help_text='Yes')
    IVA = forms.CharField(label=None , max_length =15, widget=forms.TextInput(attrs={'class': 'form-control base-height','placeholder':'IVA'}), help_text='Yes')
    via = forms.CharField(label=None , max_length =50, widget=forms.TextInput(attrs={'class': 'form-control base-height very-light-top-margin','placeholder':'Via'}), help_text='Yes')
    stelle = forms.CharField(label=None , widget=forms.TextInput(attrs={'class': 'form-control base-height very-light-top-margin','placeholder':'Quante stelle'}), help_text='Yes')
    costoCamera = forms.CharField(label=None , widget=forms.TextInput(attrs={'class': 'form-control base-height very-light-top-margin','placeholder':'Costo camera'}), help_text='Yes')
    camereTot = forms.CharField(label=None , widget=forms.TextInput(attrs={'class': 'form-control base-height very-light-top-margin','placeholder':'Camere totali'}), help_text='Yes')
    my_hidden = forms.CharField(widget=forms.HiddenInput())
    piscina = forms.BooleanField(label='Piscina',label_suffix='')
    idro = forms.BooleanField(label='Idro',label_suffix='')
    palestra = forms.BooleanField(label='Palestra',label_suffix='')
    descrizione = forms.CharField(label=None, widget=forms.Textarea(attrs={'class': 'form-control light-top-margin no-resize','placeholder':'Descrizione'}), help_text='No')