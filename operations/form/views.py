from django.shortcuts import render

def home(request):
    if (request.method=='GET'):
        return render(request,'home.html')

def addition(request):
    if (request.method=='GET'):
        return render(request,'addition.html')
    if (request.method=='POST'):
        print(request.POST)
        n1=request.POST['n1']
        n2=request.POST['n2']
        s=int(n1)+int(n2)
        print(s)
        context={'result':s}
        return render(request,'addition.html',context)
