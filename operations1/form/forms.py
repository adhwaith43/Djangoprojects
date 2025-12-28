from django import forms

class AdditionForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()


class BMIForm(forms.Form):
    weight=forms.IntegerField()
    height=forms.IntegerField()

class FactForm(forms.Form):
    num1=forms.IntegerField()

    