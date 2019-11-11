from django import forms
from .models import Video

class SearchForm (forms.Form):
    word = forms.CharField(label='Search Word')

class VideoForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    videofile = forms.CharField(max_length=200)
    class Meta:
        model= Video
        fields= ["name", "videofile"]