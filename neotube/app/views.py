from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.template.response import TemplateResponse
from .forms import *
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from .models import *
from django.forms.utils import ErrorList

# Create your views here.
def index(request):
    return render(request, 'main.html')

def signup(request):
    try_again = ""
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
            try_again = True
            print("Oops")
    else:
        form = UserCreationForm()
    args = dict()
    args['form'] = form
    if try_again != "":
        args['error'] = try_again
    return TemplateResponse(request, 'signup.html', args)

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
	#videofile=lastvideo.videofile

	form= VideoForm(request.POST)
	if form.is_valid():
		form.save()
	"""
	context= {'videofile': videofile,
				'form': form
			}
	"""
	context= {
				'form': form
			}

	return render(request, 'videos.html', context)

class VideoDetailView(DetailView):
    queryset = Video.objects.all()



class VideoListView(ListView):

    paginate_by = 10  # <app>/<modelname>_list.html 

    def get_queryset(self, *args, **kwargs):
        qs = Video.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(Video_Description__icontains=query) | Q(videofile__icontains=query))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(VideoListView, self).get_context_data(*args, **kwargs)

        return context