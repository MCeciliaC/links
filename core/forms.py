from django import forms
from django.contrib.auth.models import User
from core.models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model= Link
        fields= ['name', 'text', 'link', 'img', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.TextInput(attrs={'class':'form-control'}),
            'link': forms.TextInput(attrs={'class':'form-control'}),   
            'img': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Numero telefónico'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }

        labels = {
                'name':'Nombre', 'text': 'Descripcion', 'link':'URL sitio', 'category': 'Categoria'
            }

