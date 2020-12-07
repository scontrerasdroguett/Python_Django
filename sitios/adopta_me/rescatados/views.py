from django.shortcuts import render
from .models import Rescatado

# Create your views here.
def rescatados(request):
    rescatados = Rescatado.objects.all()
    return render(request, "rescatados/rescatados.html", {'rescatados':rescatados})