from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'hereglegch/index.html')

def burtgel(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            newUser = User.objects.create_user(form.cleaned_data['username'], '', form.cleaned_data['password1'])
            newUser.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'hereglegch/burtgel.html', {'form': form})