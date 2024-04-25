from django import forms
<<<<<<< HEAD
from . import models

#class ProductoCategoriaForm(forms.Form):
#    name = forms.CharField()
#    description = forms.CharField()
=======

from . import models

# class ProductoCategoriaForm(forms.Form):
#     nombre = forms.CharField()
#     descripcion = forms.CharField()

>>>>>>> 7a31654625695f762d69b3c101522cde5b3a90d4

class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ProductoCategoria
<<<<<<< HEAD
        fields = "__all__"
=======
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }
>>>>>>> 7a31654625695f762d69b3c101522cde5b3a90d4
