from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def blog(request):
    posts = Post.objects.all()

    page = request.GET.get('page',1)
    paginator = Paginator(posts, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/blog.html",{'posts' :posts})

def category(request, category_id):
    category = get_object_or_404(Category,id=category_id)
    return render(request, "blog/category.html", {'category':category})
