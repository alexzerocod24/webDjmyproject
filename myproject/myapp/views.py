from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Первый проект на Django.</h1>")

def new(request):
    return HttpResponse("<h1>Вторая страница моего проекта на Django.</h1>")

def data(request):
    return HttpResponse("<h1>Это страница данных на Django.</h1>")

def test(request):
    return HttpResponse("<h1>Это страница тестов на Django.</h1>")