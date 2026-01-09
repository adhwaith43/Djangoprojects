from django.shortcuts import render,redirect
from app.forms import SignupForm,AddschoolForm, StudentForm
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
        form_instance=AddschoolForm()
        context={'form':form_instance}
        return render(request,'addschool.html', context)
    
    def post(self,request):
        form_instance = AddschoolForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('app:home')
        else:
            print(form_instance.errors)


from app.models import School,Student
class Viewschool(View):
    def get(self,request):
        s=School.objects.all() # to retreive all the data
        context={'schools':s}
        return render(request,'viewschool.html',context)

class SchoolDetail(View):
    def get(self,request,i):
        can_join=True #assuming the current user has not joined in any school
        is_student=False #assuming the current is not joined in that particular school
        u=request.user
        s=School.objects.get(id=i) # to retreive all the data
        try:
            st=Student.objects.get(user=u)
            print(st)
            can_join=False
            if st.school == s:
                is_student=True
        except:
            pass

        print(can_join,is_student)
        context={'school':s,'is_student':is_student,'can_join':can_join}
        return render(request,'schooldetail.html',context)

class Studentjoin(View):
    def get(self,request):
        form_instance=StudentForm()
        context={'form':form_instance}
        return render(request,'studentjoin.html',context)
    

    def post(self,request,i):
        form_instance=StudentForm(request.POST)

        u=request.user # currently logged in user oject
        sc=School.objects.get(id=i)

        if form_instance.is_valid():
            s=form_instance.save(commit=False)
            s.user=u
            s.school=sc
            s.save()
            return redirect('app:viewschool')
        else:
            print(form_instance.errors)

class LeaveSchool(View):
    def get(self,request):
        u=request.user
        st=Student.objects.get(user=u)
        st.delete()
        return redirect('app:viewschool')