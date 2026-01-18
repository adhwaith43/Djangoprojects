from django import forms
from shop.models import Category, CustomUser
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    gender_choices=(('male','Male'),('female','Female'))
    role_choices=(('admin','Admin'),('user','User'))
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    role=forms.ChoiceField(choices=role_choices)
    class Meta:
        model = CustomUser
        fields = ['username','password1', 'password2','email','phone','gender','role']  # password2-confirm password


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AddcategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

from django import forms
from .models import Product

class AddproductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price', 'stock', 'category']



class EditproductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['stock']

