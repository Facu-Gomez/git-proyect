from django.urls import path

app_name = "cliente"

from . import views

urlpatterns = [
    # path("home/", views.home),
    path("", views.home, name="home"),
    path("cliente/create/", views.cliente_create, name="cliente_create"),
]
