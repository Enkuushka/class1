from django.shortcuts import render
from django.http import HttpResponse

from .models import Medee

def index(request):
    latest_five_news = Medee.objects.order_by('-pub_date')[:5]
    output = ', '.join([n.title for n in latest_five_news])
    return HttpResponse(output)