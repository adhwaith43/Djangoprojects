from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def factorial(request):
    if (request.method=="GET"):
        print(request.POST)
        return render(request,'factorial.html')
    if (request.method=="POST"):
        n=request.POST['n']
        fact=1
        n=int(n)
        for i in range(1,n+1):
            fact=fact*i
        context={'result':fact,'n':n}
        return render(request,'factorial.html',context)
    
def bmi(request):
    if (request.method=="GET"):
        print(request.POST)
        return render(request,'bmi.html')
    if (request.method=="POST"):
        w=request.POST['w']
        h=request.POST['h']
        result=int(w)/((int(h)/100)**2)
        context={'result':result, 'n1':w ,'n2':h}
        return render(request,'bmi.html',context)
         
    



# Create your views here.
