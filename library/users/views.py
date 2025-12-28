from django.shortcuts import render,redirect
from django.http import HttpResponse

def register(request):
    return render(request,'userregister.html')
def userLogin(request):
    return render(request,"userLogin.html")
def userlogout(request):
    return redirect('users:userlogin')

