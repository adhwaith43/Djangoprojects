from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def third(request):
    return HttpResponse('This is the third Page')

def fourth(request):
    return HttpResponse('This is the fourth Page')