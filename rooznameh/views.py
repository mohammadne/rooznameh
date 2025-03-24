# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello from Home!")
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")
