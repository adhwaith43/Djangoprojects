from django import forms
from employee.models import Employee

class Addemployees(forms.Form):
    class Meta:
        model=Employee
        fields='__all__'
