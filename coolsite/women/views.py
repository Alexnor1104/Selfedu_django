from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import AddPostForm
from .models import *

# Create your views here.
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    posts = Women.objects.all()
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница',
               'cat_selected': 0,
               }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.slug,
    }

    return render(request, 'women/post.html', context=context)


class ShowCat(View):

    def get(self, request, slug):
        category = Women.objects.filter(slug=slug)

        context = {'category': category,
                   'menu': menu,
                   'title': 'Отображение по рубрикам',
                   'cat_selected': category,
                   }
        return render(request, 'women/index.html', context=context)
