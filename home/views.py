from django.shortcuts import render, redirect
from home.models import Todo
# Create your views here.

def index(request):
    if request.POST:
        title = request.POST.get('title')
        time = request.POST.get('time')
        doc = request.POST.get('doc')
        status = request.POST.get('status')
        Todo.objects.create(title=title, time=time, doc=doc, status=status)

        return redirect("/")

    return render(request, "index.html")
