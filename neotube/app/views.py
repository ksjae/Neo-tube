from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.views.generic.edit import FormView
from .models import *

# Create your views here.
def index(request):
    return render(request, 'main.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class SearchFormView(): 
	form_class = SearchForm 
	template_name = 'video/search.html'

	def form_valid(self,form): 
		word = '%s' %self.request.POST['word'] # 검색어
		video_list = Video.title.filter( 
        Q(title__icontains=word) | Q(content__icontains=word)  # Q 객체를 사용해서 검색한다.
		# title,context 칼럼에 대소문자를 구분하지 않고 단어가 포함되어있는지 (icontains) 검사
		 ).distinct() #중복을 제거한다. 
		context = {}
		context['object_list'] = video_list # 검색된 결과를 컨텍스트 변수에 담는다. 
		context['search_word']= word # 검색어를 컨텍스트 변수에 담는다.
		return context

# Create your views here.
def showvideo(request):
	lastvideo= Video.objects.last()
	videofile=lastvideo

	form= VideoForm(request.POST)
	if form.is_valid():
		form.save()

	context= {'videofile': videofile,
				'form': form
			}

	return render(request, 'neotube/videos.html', context)