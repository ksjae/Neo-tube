from django import forms
from .models import Video
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class SearchForm (forms.Form):
    word = forms.CharField(label='Search Word')

class VideoForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    videofile = forms.CharField(max_length=200)
    class Meta:
        model= Video
        fields= ["name", "videofile"]

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.Field(widget=forms.TextInput(
        attrs={'class':"form-control", 'id':"username", 'aria-describedby':"emailHelp", 'placeholder':"아이디 입력"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':"form-control", 'id':"password", 'aria-describedby':"emailHelp", 'placeholder':"비밀번호 입력"}))
