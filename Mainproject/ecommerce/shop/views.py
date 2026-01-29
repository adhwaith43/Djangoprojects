from django.shortcuts import render, redirect
from django.views import View

from shop.models import Category,Product


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



# admin home
class AdminHome(View):
    def get(self,request):
        return render(request,'adminhome.html')
    
# user home
class Userhome(View):
    def get(self,request):
        return render(request,'userhome.html')


from shop.forms import SignupForm, LoginForm,EditproductForm
# Register
class Register(View):
    def get(self, request):
        form_instance = SignupForm()
        context = {"form": form_instance}
        return render(request, 'userregister.html', context)

    def post(self, request):
        form_instance = SignupForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:userlogin')
        else:
            print(form_instance.errors)


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


class Userlogin(View):
    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            print(data)
            u = data['username']
            p = data['password']

            user = authenticate(username=u, password=p)

            if user and user.is_superuser==True:
                login(request, user)
                return redirect('shop:adminhome')
            
            elif user and user.role == "user":
                login(request,user)
                return redirect('shop:userhome')
            else:
                messages.error(request, "Invalid User credentials")
                return redirect('shop:userlogin')
            

    def get(self, request):
        form_instance = LoginForm()
        context = {"form": form_instance}
        return render(request, 'userlogin.html', context)


class Userlogout(View):
    def get(self, request):
        logout(request)  # removes the current user from the session
        return redirect('shop:userlogin')
    

from shop.forms import AddcategoryForm, AddproductForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#decorator required -admin_requied
def admin_required(fun):
    def wrapper(request):
        if not request.user.is_supersuer:
            return HttpResponse("Admin User Only")
        else:
            return fun(request)
    return wrapper

@method_decorator(admin_required,name="dispatch")
@method_decorator(login_required,name="dispatch")
class AddCategory(View):
    def get(self, request):
        form_instance = AddcategoryForm()
        context = {"form": form_instance}
        return render(request, 'addcategory.html', context)

    def post(self, request):
        form_instance = AddcategoryForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:addcategories')
        else:
            print(form_instance.errors)

@method_decorator(admin_required,name="dispatch")
@method_decorator(login_required,name="dispatch")
# Add Product
class AddProduct(View):
    def get(self, request):
        form_instance = AddproductForm()
        context = {"form": form_instance}
        return render(request, 'addproduct.html', context)

    def post(self, request):
        form_instance = AddproductForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:addproducts')
        else:
            print(form_instance.errors)

class ProductDetail(View):
    def get(self,request,i):
        p=Product.objects.get(id=i)
        context={'product':p}
        return render(request,'productdetail.html',context)
    

class Editproduct(View):
    def get(self,request,i):
        b=Product.objects.get(id=i)
        form_instance=EditproductForm(instance=b)
        context={'form':form_instance}
        return render(request,'editproducts.html',context)
    
    def post(self,request,i):
        p=Product.objects.get(id=i)
        form_instance =EditproductForm(request.POST,instance=p)
        if form_instance.is_valid():
                form_instance.save()
                return redirect('shop:categories')


from cart.models import Order
class Yourorders(View):
    def get(self,request):
        o=Order.objects.filter(user=request.user,is_ordered=True)
        context={'orders':o}
        return render(request,'ordersummary.html',context)