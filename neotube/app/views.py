from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.template.response import TemplateResponse
from .forms import *
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'main.html')

def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = NewUserForm()
    args = dict()
    args['form'] = form
    return TemplateResponse(request, 'signup.html', args)

class SearchFormView(FormView): 
	form_class = SearchForm 
	template_name = 'search.html'

	def form_valid(self,form): 
		word = '%s' %self.request.POST['word'] # 검색어
		video_list =Video.objects.filter((Q(title__icontains=word) | Q(id__icontains=word) | Q(uploader__icontains=word))  # Q 객체를 사용해서 검색한다.
		# title,context 칼럼에 대소문자를 구분하지 않고 단어가 포함되어있는지 (icontains) 검사
		 ).distinct() #중복을 제거한다. 
		context = {}
		context['object_list'] = video_list # 검색된 결과를 컨텍스트 변수에 담는다. 
		context['search_word'] = word # 검색어를 컨텍스트 변수에 담는다.
		context['form'] = form
		return render(self.request,self.template_name,context)

# Create your views here.
def showvideo(request):
	lastvideo= Video.objects.last()
	videofile=lastvideo

	form= VideoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.pub_date = 
		form.save()
	
	context= {'videofile': videofile,
				'form': form
			}
	"""
	context= {
				'form': form
			}
	"""
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