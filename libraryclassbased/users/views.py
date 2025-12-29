
from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.forms import SignupForm
from users.forms import LoginForm
from django.views import View


# def register(request):
#     return render(request,'userregister.html')
# def userLogin(request):
#     return render(request,"userLogin.html")
# def userlogout(request):
#     return redirect('users:userlogin')


class Register(View):
    def get(self,request):
        form_instance=SignupForm()
        context={"form":form_instance}
        return render(request,'userregister.html',context)
    
    def post(self,request):
        form_instance=SignupForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:userlogin')
        else:
            print(form_instance.errors)
    
from django.contrib.auth import authenticate,login,logout
class Userlogin(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            u=data['username'] #reads the username from cleaned data and assigns to variable u
            p=data['password'] #reads the username from cleaned data and assigns to variable p
                               #authenticate/login/logout --built in functions deafined inside contrib.auth module
            user=authenticate(username=u,password=p)
                   #authenticate() checks whether a user record exists in the User table
                   #matching with the submitted username and password.if yes,returns the
                   #user object ellse it returns none.

            if user:
                login(request,user)             #adds the user into the current session

                return redirect('books:home')   #redirects to the homepage

            else:
                return HttpResponse("Invalid User credentials")
            

    def get(self,request):
        form_instance=LoginForm()
        context={"form":form_instance}
        return render(request,'userlogin.html',context)
    
class Userlogout(View):
    def get(self,request):
        logout(request)    #removes the current user from the session
        return redirect('users:userlogin')


