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
        fields=('account_name','password')
        labels={'account_name':'アカウント名','password':'パスワード'}
