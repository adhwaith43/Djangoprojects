from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# function based

# class based


def home(request):
    
    return HttpResponse("Welcome to Home page")


def index(request):
    return HttpResponse("This is the index page")