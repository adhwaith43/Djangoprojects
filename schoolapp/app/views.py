from django.shortcuts import render,redirect
from app.forms import SignupForm,Addbooks
# Create your views here.
from django.views import View

class Home(View):
    def get(self,request):
        return render(request,'home.html')
class Adminhome(View):
    def get(self,request):
        return render(request,'adminhome.html')
class Studenthome(View):
    def get(self,request):
        return render(request,'studenthome.html')

class Register(View):
    def get(self, request):
        form_instance = SignupForm()
        context = {"form": form_instance}
        return render(request, 'register.html', context)

    def post(self, request):
        form_instance = SignupForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('app:userlogin')
        else:
            print(form_instance.errors)

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from app.forms import LoginForm

class Userlogin(View):
    def post(self, request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            print(data)
            u = data['username']
            p = data['password']

            user = authenticate(username=u, password=p)

            if user.role == "student":
                login(request,user)
                return redirect('app:studenthome')
            
            elif user and user.role== "admin":
                login(request,user)
                return redirect('app:adminhome')

            else:
                messages.error(request, "Invalid User credentials")
                return redirect('app:userlogin')
            

    def get(self, request):
        form_instance = LoginForm()
        context = {"form": form_instance}
        return render(request, 'login.html', context)


class Userlogout(View):
    def get(self, request):
        logout(request)  # removes the current user from the session
        return redirect('app:userlogin')

class Addschool(View):
    def get(self,request):
        form_instance=Addbooks()
        context={'form':form_instance}
        return render(request, 'addschool.html', context)
    
    def post(self,request):
        form_instance = Addbooks(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('app:home')
        else:
            print(form_instance.errors)



