from django import forms
from .models import Post,Creater

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text')

class SignupForm(forms.ModelForm):
    class Meta:
        model=Creater
        fields=('creater_name','creater_pass')
