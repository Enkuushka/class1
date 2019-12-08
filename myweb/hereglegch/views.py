from django.shortcuts import render

from django.contrib.auth.models import User

def index(request):
    return render(request, 'hereglegch/index.html')