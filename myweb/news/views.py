from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from datetime import datetime

from .models import Medee, LikeCounter

def index(request):
    latest_five_news = Medee.objects.order_by('-pub_date')[:5]
    output = ', '.join([n.title for n in latest_five_news])
    return render(request, "news/index.html", {"data": latest_five_news})

@login_required
def read(request, news_id):
    news = Medee.objects.get(pk=news_id)
    return render(request, "news/read.html", {"news": news})
    

@login_required
def like(request, news_id):
    news = Medee.objects.get(pk=news_id)
    likeObj = LikeCounter.objects.filter(user_id = request.user.id, medee_id = news_id)
    if(likeObj.count() == 0):
        news.liketoo = news.liketoo + 1
        news.save(update_fields = ['liketoo'] )

        likeObj = LikeCounter()
        likeObj.user_id = request.user.id
        likeObj.medee_id = news.id
        likeObj.liked_date = datetime.now()
        likeObj.save()

        return HttpResponse(news.liketoo)
    else:
        return HttpResponse(news.liketoo)