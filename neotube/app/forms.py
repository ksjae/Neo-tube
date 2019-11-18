from django import forms
from .models import Video
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class SearchForm(forms.Form):
    word = forms.CharField(label='Search Word')

class VideoForm(forms.ModelForm):
    """
    name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class':"form-control", 'id':"name", 'placeholder':"영상 제목 입력"}))
    videofile = forms.FileField(upload_to='media/videos/%Y/%m/%d/', null=True, verbose_name="")
    slug = forms.SlugField(unique=True)
    timestamp   = forms.DateTimeField(auto_now_add=True)
    """
    name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class':"form-control", 'id':"name", 'placeholder':"영상 제목 입력"}))
    class Meta:
        model= Video
        fields= ["name", "videofile"]
        ordering = ['-timestamp']
    
    def get_absolute_url(self):
        return reverse("deploy:detail", kwargs={"slug":self.slug})

    def __str__(self):
        return self.Video_Description + ": " + str(self.id)

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.Field(widget=forms.TextInput(
        attrs={'class':"form-control", 'id':"username", 'aria-describedby':"emailHelp", 'placeholder':"아이디 입력"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':"form-control", 'id':"password", 'aria-describedby':"emailHelp", 'placeholder':"비밀번호 입력"}))

class NewUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)

    username = forms.Field(widget=forms.TextInput(
        attrs={'class':"form-control", 'id':"username", 'aria-describedby':"emailHelp", 'placeholder':"이메일도 가능"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':"form-control", 'id':"password", 'aria-describedby':"emailHelp", 'placeholder':"8자 이상"}))

