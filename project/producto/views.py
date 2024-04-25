from django.shortcuts import redirect, render
<<<<<<< HEAD
=======

from . import forms, models
>>>>>>> 7a31654625695f762d69b3c101522cde5b3a90d4

from . import models, forms

def home(request):
<<<<<<< HEAD
    if request.GET["consulta"]:
        consulta = request.GET["consulta"]
        query = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
    else:        
        query = models.ProductoCategoria.objects.all()
=======
    # if request.GET["consulta"]:
    # consulta = request.GET["consulta"]
    # query = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
    # else:
    query = models.ProductoCategoria.objects.all()

>>>>>>> 7a31654625695f762d69b3c101522cde5b3a90d4
    context = {"productos": query}
    return render(request, "producto/index.html", context)


def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
<<<<<<< HEAD
        if form.is_valid():
            form.save()
            return redirect("producto:home")
    else: #request.method == "GET"
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/productocategoria_create.html", {"form": form})


        
=======
        if form.is_valid:
            form.save()
            return redirect("producto:home")
    else:  # request.method == "GET"
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/productocategoria_create.html", context={"form": form})
>>>>>>> 7a31654625695f762d69b3c101522cde5b3a90d4
