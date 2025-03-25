from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post

# Create your views here.


def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts_list.html', {'posts': posts})


def post(request, slug):
    # return HttpResponse(slug)
    posts = Post.objects.get(slug=slug)
    return render(request, 'post_page.html', {'post': post})
