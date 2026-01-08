from django.shortcuts import render
from django.views import View
from app.models import Place
# Create your views here.

class Home(View):
    def get(self,request):
        p=Place.objects.all()
        context={'places':p}
        return render(request,'home.html',context)
