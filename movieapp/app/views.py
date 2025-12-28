from django.shortcuts import render,redirect

from app.forms import Addmovies
from app.models import Movie
# Create your views here.

# def home(request):
#     return render(request,'home.html')
def viewMovies(request):
    # processing code to retrieve data
    m=Movie.objects.all()# returns sequence of db objects/records
    print(m)
    context={'movies':m}
    return render(request,"home.html",context)

def addmovie(request):
    if (request.method=='GET'):
        form_instance=Addmovies()
        context={'form':form_instance}
        return render(request,'addmovie.html',context)
    if (request.method=='POST'):
        # create form_instance with submitted data
        form_instance =Addmovies(request.POST,request.FILES)
        print(request.POST)
        print(request.FILES)

        # checks validity of data
        if (form_instance.is_valid()):
            form_instance.save()
            # return render(request,'addbooks.html')
            return redirect('viewMovies')


