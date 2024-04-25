from django.shortcuts import redirect, render
from . import models, forms

# Create your views here.
from . import models


def home(request):
    consulta_clientes = models.Cliente.objects.all()
    context = {"clientes": consulta_clientes}
    return render(request, "cliente/index.html", context)

def cliente_create(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:home")
    else:
        form = forms.ClienteForm()
    return render(request, "cliente/cliente_crear.html", {"form": form})
