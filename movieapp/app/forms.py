from django import forms

# class Addbooks(forms.Form):
#     title=forms.CharField()
#     author=forms.CharField()
#     price=forms.IntegerField()
#     pages=forms.IntegerField()
#     language=forms.CharField()

from app.models import Movie

class Addmovies(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'