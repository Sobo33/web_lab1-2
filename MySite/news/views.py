from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', context)

def test(request):
    print(request)
    return HttpResponse('TEST')
# Create your views here.
