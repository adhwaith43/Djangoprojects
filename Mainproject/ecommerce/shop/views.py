from django.shortcuts import render
from django.views import View

from shop.models import Category


#ALL Categories
class CategoryView(View):
    def get(self,request):
        c=Category.objects.all()
        context={"categories": c}
        return render(request,'categories.html',context)

#ALL products under a specific category  
class Categoryproducts(View):
    def get(self,request,i):#here i is category id
        c=Category.objects.get(id=i)
        context={'category':c}
        return render(request,'products.html',context)
