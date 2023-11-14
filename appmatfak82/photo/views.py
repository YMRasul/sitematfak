from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404,StreamingHttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from appmatfak82 import settings

# Главное меню
menu  = [{'title':'Главная страница','url_name':'home'},
         {'title':'Альбом',           'url_name':'category' },
         {'title':'Видео',          'url_name':'videoapp'},
         {'title':"О сайте",        'url_name':'about'},
         {'title':"Обратная связь", 'url_name':'contact'},
        ]


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')  # должны импортировать эту функцию

def home(request):   # Главная страница
    homephoto = first.objects.filter(pk=1) # только первая фотография
    cntxt ={
        'homephoto': homephoto,
        'menu': menu,
        'title': 'ТашГУ матфак82',
    }
    return render(request, 'photo/home.html', context=cntxt)
    # третьим аргументом передаем словарь cntxt


def show_category_all(request,cat_id):
    mphoto = photo.objects.filter(cat_id=cat_id)
    cats = categ.objects.all()
    if len(mphoto) == 0:
        raise Http404()

    cntxt = {
            'mphoto': mphoto,
            'cats': cats,
            'menu': menu,
            'title': 'ТашГУ матфак82',
            'cat_selected': cat_id,
    }
    return render(request, 'photo/mphoto.html', context=cntxt)

def show_category(request):
    mphoto = photo.objects.filter(pk=1)
    cats = categ.objects.all()
    print(cats)
    cntxt = {
            'mphoto': mphoto,
            'cats': cats,
            'menu': menu,
            'title': 'ТашГУ матфак82',
#            'cat_selected': cat_id,
    }
    #return render(request, 'photo/temp.html', {'menu': menu,'title': 'Отображение категори'})
    return render(request, 'photo/mphoto.html',  context=cntxt)

def videos(request):
    return render(request, 'photo/about.html', {'menu': menu,'title': 'Видеолар'})

def about(request):
    return render(request, 'photo/about.html', {'menu': menu,'title': 'О сайте'})

def contact(request):
    return render(request, 'photo/about.html', {'menu': menu,'title': 'Контакты'})
