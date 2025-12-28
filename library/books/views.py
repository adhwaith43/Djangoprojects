from django.shortcuts import render,redirect
# from django.http import HttpResponse

from books.forms import Addbooks
from books.models import Book
def home(request):
    return render(request,'home.html')


def addBooks(request):
    if (request.method=='GET'):
        form_instance=Addbooks()
        context={'form':form_instance}
        return render(request,'addbooks.html',context)
    
    if (request.method=='POST'):
        # create form_instance with submitted data
        form_instance =Addbooks(request.POST,request.FILES)
        print(request.POST)
        print(request.FILES)

        # checks validity of data
        if (form_instance.is_valid()):
            # data=form_instance.cleaned_data # taking data for processing

            # # inserting into table
            # b=Book.objects.create(**data)
            # # saving the data 
            # b.save()
            form_instance.save()
            # return render(request,'addbooks.html')
            return redirect('books:viewbooks')

def viewBooks(request):
    # processing code to retrieve data
    b=Book.objects.all()# returns sequence of db objects/records
    print(b)
    context={'books':b}
    return render(request,"viewbooks.html",context)

def detail(request,i):
    if (request.method=='GET'):
        b=Book.objects.get(id=i)
        context={'book':b}
        return render(request,'detail.html',context)

def delete(request,i):
    if (request.method=='GET'):
        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:viewbooks')
    
def edit(request,i):
    if (request.method=='GET'):
        b=Book.objects.get(id=i)
        form_instance=Addbooks(instance=b)
        context={'form':form_instance}
        return render(request,'edit.html',context)

    