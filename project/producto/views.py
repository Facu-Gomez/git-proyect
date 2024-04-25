from django.shortcuts import redirect, render

from . import models, forms

def home(request):
    query = models.ProductoCategoria.objects.all()
    if "consulta" in request.GET:  
        consulta = request.GET["consulta"]
        query = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
    else:        
        query = models.ProductoCategoria.objects.all()
    context = {"productos": query}
    return render(request, "producto/index.html", context)


def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:home")
    else: #request.method == "GET"
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/productocategoria_create.html", {"form": form})


        
