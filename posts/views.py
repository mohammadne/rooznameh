from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts_list.html', {'posts': posts})
