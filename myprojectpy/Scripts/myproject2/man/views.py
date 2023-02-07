from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden, HttpResponseServerError, \
    HttpResponseBadRequest
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse('bla bla')

def categories(request, catid):
    if request.Post:
     print(request.Post)
    return HttpResponse(f"<h1>bla bla</h1><p>{catid}</p>")

def archive(request, year):
    if int(year)>2022:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1> Archive po godam</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>stranitsa ne naidena</h1>')

def pageForbidden(request, exception):
    return HttpResponseForbidden('stranitsa forbidden')

def pageServerError(request,):
    return HttpResponseServerError('server error')

def pageBadRequest(request, exception):
    return HttpResponseBadRequest('Bad Request')