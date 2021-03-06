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
        model = Video
        fields = ["name", "videofile"]

    def __str__(self):
        return self.Video_Description + ": " + str(self.id)