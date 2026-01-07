from django.core.mail import send_mail
from django.shortcuts import render, redirect
from users.forms import SignupForm
from users.forms import LoginForm
from django.views import View

class Home(View):
    def get(self,request):
        return render(request,'home.html')
class AdminHome(View):
    def get(self,request):
        return render(request,'adminhome.html')
class StudentHome(View):
    def get(self,request):
        return render(request,'studenthome.html')
class TeacherHome(View):
    def get(self,request):
        return render(request,'Teacherhome.html')

from django.core.mail import send_mail

class Register(View):
    def get(self, request):
        form_instance = SignupForm()
        context = {"form": form_instance}
        return render(request, 'register.html', context)

    def post(self, request):
        form_instance = SignupForm(request.POST, request.FILES)
        if form_instance.is_valid():
            # form_instance.save()
            # return redirect('users:userlogin')

            u=form_instance.save()
            u.is_active=False
            u.save()
            u.generate_otp()

            send_mail("Django auth otp",
                        u.otp,
                      "adhwaitham04@gmail.com",
                      [u.email],
                      fail_silently=True)
            return redirect('users:otpverify')
        
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
                return redirect('users:adminhome')
            
            elif user and user.role == "student":
                login(request,user)
                return redirect('users:studenthome')
            
            elif user and user.role== "teacher":
                login(request,user)
                return redirect('users:teacherhome')

            else:
                messages.error(request, "Invalid User credentials")
                return redirect('users:userlogin')
            

    def get(self, request):
        form_instance = LoginForm()
        context = {"form": form_instance}
        return render(request, 'login.html', context)


class Userlogout(View):
    def get(self, request):
        logout(request)  # removes the current user from the session
        return redirect('users:userlogin')
from users.models import CustomUser
class Otpverify(View):
    def post(self,request):
        otp=request.POST['o']
        try:
            c=CustomUser.objects.get(otp=otp)
            c.is_active=True
            c.is_verified=True
            c.otp=None
            c.save()
            return redirect("users:userlogin")
        except:
            messages.error(request,'invalid otp')
            return redirect('users:otpverify')
        
    def get(self,request):
        return render(request,'otpverify.html')