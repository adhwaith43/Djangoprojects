from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('First page')

def second(request):
    return HttpResponse('Second page')