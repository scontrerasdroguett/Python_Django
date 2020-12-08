from django.shortcuts import render
from .models import Rescatado
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def rescatados(request):
    rescatados = Rescatado.objects.all()

    page = request.GET.get('page',1)
    paginator = Paginator(rescatados, 5)

    try:
        rescatados = paginator.page(page)
    except PageNotAnInteger:
        rescatados = paginator.page(1)
    except EmptyPage:
        rescatados = paginator.page(paginator.num_pages)

    return render(request, "rescatados/rescatados.html", {'rescatados':rescatados})