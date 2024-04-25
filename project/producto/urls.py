from django.urls import path

app_name = "producto"

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("productocateforia/create/", views.productocategoria_create, name="productocategoria_create"),
]
