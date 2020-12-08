from django.shortcuts import render, HttpResponse

html_nav="""
<h1>Mi web</h1>
<ul>
    <li> <a href="/">Home</li></a>
    <li> <a href="/about/">About</li></a>
    <li> <a href="/contact/">Contact</li></a>
    <li> <a href="/rescatados/">Rescatados</li></a>
</ul>
"""


# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def visit(request):
    return render(request, "core/visit.html")
