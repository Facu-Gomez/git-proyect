from django import forms
from . import models

#class ProductoCategoriaForm(forms.Form):
#    name = forms.CharField()
#    description = forms.CharField()

class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ProductoCategoria
        fields = "__all__"