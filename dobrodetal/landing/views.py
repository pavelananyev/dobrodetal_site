from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


def getout(request):
    out = ''
    if request.GET:
        getdict = request.GET
        for key, val in getdict.items():
            out += f'<p>Ключ: {key}; значение: {val}</p>'
        print(request.GET)
        print(out)
    return out


# Create your views here.
def main(request):
    gout = getout(request)
    return HttpResponse(f'Поставка запчастей для сельхозтехники' + bool(gout) * f'<p>GET запрос:</p><p>{gout}</p>')


def contact(request):
    gout = getout(request)
    return HttpResponse(f'Контакты' + bool(gout) * f'<p>GET запрос:</p><p>{gout}</p>')


def pageNotFound(request, exception):
    # return HttpResponseNotFound('<h1>Страница не найдена</h1>')
   return redirect('home', permanent=True)
