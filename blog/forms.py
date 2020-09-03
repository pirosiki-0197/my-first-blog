from django import forms
from .models import Post,Creater

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text')
        labels={'title':'タイトル','text':'本文'}

class SignupForm(forms.ModelForm):
    class Meta:
        model=Creater
        fields=('username','password')
        labels={'username':'アカウント名','password':'パスワード'}

class Make_account(forms.Form):
    name=forms.CharField(max_length=20)
    pw=forms.CharField(max_length=20)
