from django.urls import path

from . import views

app_name = "producto"


urlpatterns = [
    path("", views.home, name="home"),
<<<<<<< HEAD
    path("productocateforia/create/", views.productocategoria_create, name="productocategoria_create"),
=======
    path("productocategoria/create/", views.productocategoria_create, name="productocategoria_create"),
>>>>>>> 7a31654625695f762d69b3c101522cde5b3a90d4
]
