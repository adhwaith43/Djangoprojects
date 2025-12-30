from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Customuser

class SignupForm(UserCreationForm):
    gender_choices=[('male','Male'),("female","Female")]
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    
    class Meta:
        model=Customuser
        fields=['username','password1','first_name','last_name','password2','phone','address'] #password2-confirm password
        
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)