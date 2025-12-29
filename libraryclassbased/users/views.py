
from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.forms import SignupForm
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
    
class UserLogin(View):
    def get(self,request):
        return render(request,"userLogin.html")
class Userlogout(View):
    def get(self,request):
        return redirect('users:userlogin')

