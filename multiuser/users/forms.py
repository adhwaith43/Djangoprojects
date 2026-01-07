from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    gender_choices=(('male','Male'),('female','Female'))
    role_choices=(('student','Student'),('teacher','Teacher'))
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    role=forms.ChoiceField(choices=role_choices)
    class Meta:
        model = CustomUser
        fields = ['username','password1', 'password2','email','phone','gender','role']  # password2-confirm password


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)