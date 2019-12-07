from django.shortcuts import render
from django.http import HttpResponse

from .models import Medee

def index(request):
    latest_five_news = Medee.objects.order_by('-pub_date')[:5]
    output = ', '.join([n.title for n in latest_five_news])
    return render(request, "news/index.html", {"data": latest_five_news})

def read(request, news_id):
    news = Medee.objects.get(pk=news_id)
    return render(request, "news/read.html", {"news": news})

def like(request, news_id):
    news = Medee.objects.get(pk=news_id)
    news.liketoo = news.liketoo + 1
    news.save(update_fields = ['liketoo'] )
    return HttpResponse(news.liketoo)