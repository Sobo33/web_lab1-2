from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    return HttpResponse('Hello world')

def test(request):
    print(request)
    return HttpResponse('TEST')
# Create your views here.
