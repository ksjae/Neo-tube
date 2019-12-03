from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.template.response import TemplateResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import Q
from django.utils.text import slugify
import random, string
import datetime

# Create your views here.


def index(request):
    return render(request, 'main.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    args = dict()
    args['form'] = form
    return TemplateResponse(request, 'signup.html', args)


class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'search.html'

    def form_valid(self, form):
        word = '%s' % self.request.POST['word']  # 검색어
        video_list = Video.objects.filter((Q(name__icontains=word) | Q(uploader__icontains=word))  # Q 객체를 사용해서 검색한다.
        # title,context 칼럼에 대소문자를 구분하지 않고 단어가 포함되어있는지 (icontains) 검사
        ).distinct().order_by('pub_date')  # 중복을 제거한다.
        # video_list = Video.objects.all().distinct()
        for i in video_list:
            print(i.name)
        context = {}
        print(word)
        context['object_list'] = video_list  # 검색된 결과를 컨텍스트 변수에 담는다.
        context['search_word'] = word  # 검색어를 컨텍스트 변수에 담는다.
        context['form'] = form
        return render(self.request, self.template_name, context)

# Create your views here.


def uploadvideo(request):
    lastvideo = Video.objects.last()
    videofile = lastvideo

    raw_form = VideoForm(request.POST or None, request.FILES or None)
    if raw_form.is_valid():
        form = raw_form.save(commit=False)
        form.pub_date = datetime.datetime.now()
        form.name = raw_form.cleaned_data['name']
        form.uploader = request.user.get_username()
        if form.uploader == "":
            form.uploader = "로그인하지 않은 이용자"
        form.views = 0
        slug = slugify(form.name, allow_unicode=True)
        qs_exists = Video.objects.filter(slug=slug).exists()
        if qs_exists:
            new_slug = "{slug}-{randstr}".format(
                        slug=slug,
                        randstr=''.join(random.choice(string.ascii_lowercase) for i in range(4))
                    )
            slug = slugify(new_slug, allow_unicode=True)
        form.slug = slug
        print(slug)
        form.save()
        return redirect(reverse('view', kwargs={'videofile':Video.objects.last().slug}), videofile=(Video.objects.last(),))

    context = {'videofile': videofile,
                'form': raw_form
            }
    """
    context= {
                'form': form
            }
    """
    return render(request, 'videos.html', context)


def videoview(request, videofile):
    # video = Video.objects.last()
    video_list = Video.objects.filter(slug=videofile)
    vid = list(video_list)
    if vid == []:
        return render(request, '404.html')
    Video.objects.filter(slug=videofile).update(views=vid[0].views+1)
    context={'videofile': vid[0],
            }
    
    return render(request, 'view.html', context)



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
        context=super(VideoListView, self).get_context_data(*args, **kwargs)

        return context
