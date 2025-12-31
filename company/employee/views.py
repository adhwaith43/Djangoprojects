from django.shortcuts import render,redirect

from employee.forms import Addemployees
from employee.models import Employee
from django.views import View


# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'home.html')
    
class Emloyeeregister(View):
    def get(self,request):
        form_instance=Addemployees()
        context={'form':form_instance}
        return render(request,'employeeregister.html',context)

    def post(self,request):
        form_instance=Addemployees(request.POST,request.FILES)
        if (form_instance.is_valid()):
            form_instance.save()
            return redirect('employee:viewemployee')

class Emloyeelist(View):
    def get(self,request):
        e=Employee.objects.all()
        context={'form': e}
        return render(request,'employeelist.html',context)

class Employeedetail(View):
    def get(self,request,i):
        e=Employee.objects.get(id=i)
        context={'form': e}
        return render(request,'employeedetail.html',context)

class Delete(View):
    def get(self,request,i):
        e=Employee.objects.get(id=i)
        e.delete()
        return redirect('employee:viewemployee')
    
class Employeeupdate(View):
    def get(self,request,i):
        e=Employee.objects.get(id=i)
        form_instance=Addemployees(instance=e)
            
        context={'form':form_instance}
        return render(request,'edit.html',context)
        
    def post(self,request,i):
        e=Employee.objects.get(id=i)
        form_instance =Addemployees(request.POST,request.FILES,instance=e)

        if (form_instance.is_valid()):
            form_instance.save()
            return redirect('employee:viewemployee')

