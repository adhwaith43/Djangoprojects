from django.shortcuts import render,redirect
from users.forms import Signupform
from users.forms import Loginform
from django.views import View

# Create your views here.
from django.views import View

class Register(View):
    def get(self,request):
        form_instance=Signupform()
        context={"form":form_instance}
        return render(request,'userregister.html',context)
    
    def post(self,request):
        form_instance=Signupform(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:userlogin')
        else:
            print(form_instance.errors)

from django.contrib import messages    
from django.contrib.auth import authenticate,login,logout

class Userlogin(View):
    def post(self,request):
        form_instance=Loginform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            u=data['username'] 
            p=data['password'] 
                               
            user=authenticate(username=u,password=p)
                   
            if user:
                login(request,user)            
                return redirect('employee:home')   

            else:
                messages.error(request, "Invalid User credentials")
                return redirect('users:userlogin')
            

    def get(self,request):
        form_instance=Loginform()
        context={"form":form_instance}
        return render(request,'userlogin.html',context)



class Userlogout(View):
    def get(self,request):
        logout(request)    #removes the current user from the session
        return redirect('users:userlogin')