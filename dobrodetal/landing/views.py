from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import *


def getout(request):
    out = ''
    if request.GET:
        getdict = request.GET
        for key, val in getdict.items():
            out += f'<p>Ключ: {key}; значение: {val}</p>'
        print(request.GET)
        print(out)
    return out

menu = [{'id': 1, 'name': 'Каталог', 'slag': '#catalog'},
        {'id': 2, 'name': 'Почему мы', 'slag': '#why_us'},
        {'id': 3, 'name': 'Заказать', 'slag': '#order'},
        {'id': 4, 'name': 'О нас', 'slag': '#about_us'},
        {'id': 5, 'name': 'Отзывы', 'slag': '#reviews'},
        {'id': 6, 'name': 'Контакты', 'slag': '#contacts'}
        ]


# Create your views here.
def main(request):
    details = Detail.objects.all()
    return render(request, 'landing/main.html', {'details': details, 'menu': menu, 'title': "Главная страница"})


def new(request):
    return render(request, 'landing/new.html', {'menu': menu, 'title': "Новая страница"})


def contact(request):
    gout = getout(request)
    return HttpResponse(f'Контакты' + bool(gout) * f'<p>GET запрос:</p><p>{gout}</p>')


def pageNotFound(request, exception):
    # return HttpResponseNotFound('<h1>Страница не найдена</h1>')
    return redirect('home', permanent=True)
