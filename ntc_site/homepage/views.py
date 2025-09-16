from django.shortcuts import render
from django.views.generic import ListView
from django.conf import settings

from .models import News

def homepage(request):
    template_name = 'homepage/homepage.html'
    news = News.objects.values(
        'title',
        'text',
        'created_at',
        'image',
        'id',
    ).order_by('-created_at')[:4]
    context = {
        'news': news,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, template_name, context)

def news_detail(request, pk):
    template_name = 'homepage/news_detail.html'
    news = News.objects.get(pk=pk)
    context = {
        'news': news,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, template_name, context)