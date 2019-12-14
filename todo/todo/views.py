from django.shortcuts import render
from django.http import HttpResponse

from todoapp.models import Todo

def index(request):
    return render(request, 'todo/index.html')


def getData(request):
    obj = Todo.objects.get()
    data = "empty"
    if(obj != None):
        data = obj.data
    return HttpResponse(data)


def saveData(request):
    data = request.POST.get("todoItems")
    Todo.objects.all().delete()
    obj = Todo()
    obj.data = data
    obj.save()
    return HttpResponse(data)