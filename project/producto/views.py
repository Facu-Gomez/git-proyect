from django.shortcuts import render

from . import models


def home(request):
    consulta_productos = models.ProductoCategoria.objects.all()
    context = {"productos": consulta_productos}
    return render(request, "producto/index.html", context)


def productocategoria_create(request):
    return render(request, "producto/productocategoria_create.html")