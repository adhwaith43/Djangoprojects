from django.shortcuts import render

from employee.forms import Addemployees
from employee.models import Employee
from django.views import View


# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'home.html')
    
# class Emloyeeregister(View):

# class Employeelogin(View):

# class Employeelogout(View):

# class Employeedetail(View):
    
# class Employeeupdate(View):

# class Delete(View):