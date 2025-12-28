from django import forms

class Signupform(forms.Form):
    gender_choices=(('male','Male'),('female','Female'))
    role_choices=(('admin','Admin'),('doctor','Doctor'),('patient','Patient'))

    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.CharField()
    phone=forms.IntegerField()
    age=forms.IntegerField()
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    Role=forms.ChoiceField(choices=role_choices)
