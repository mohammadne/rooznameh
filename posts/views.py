from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from .models import Post
from . import forms

# Create your views here.


def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts_list.html', {'posts': posts})


def post(request, slug):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    return render(request, 'post_page.html', {'post': post})


@login_required(login_url="/users/login")
def post_new(request):
    if request.method == "GET":
        form = forms.CreatePost()
        return render(request, 'post_new.html', {"form": form})

    form = forms.CreatePost(request.POST, request.FILES)
    if form.is_valid:
        new_post = form.save(commit=False)
        new_post.author = request.user
        new_post.save()
        return redirect("posts:list")
