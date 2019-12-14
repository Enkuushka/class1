from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

from django.utils import translation

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from todoapp.models import Todo

def index(request):
    translation.activate(request.GET.get('lang'))
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
    return HttpResponse(_("Result ok!"))


def testPdf(request):
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)

    p.drawString(100, 100, request.GET.get('name'))

    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')