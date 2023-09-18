from django.shortcuts import render, redirect
from home.models import Todo
# Create your views here.

def index(request):
    if request.POST:
        title = request.POST.get('title')
        time = request.POST.get('time')
        doc = request.POST.get('doc')
        status = request.POST.get('status')
        Todo.objects.create(title=title, time=time, description=doc, status=status)

        return redirect("/")

    data = {
        'todo': Todo.objects.all()
    }

    return render(request, "index.html", context=data)



def delete(request, id):
    Todo.objects.get(id=id).delete()

    return redirect("/")

def edit(request, id):
    if request.POST:
        title = request.POST.get('title')
        time = request.POST.get('time')
        doc = request.POST.get('doc')
        status = request.POST.get('status')
        Todo.objects.filter(id=id).update(title=title, time=time, description=doc, status=status)

        return redirect("/")

    data = {
        'todo': Todo.objects.get(id=id)
    }

    return render(request, "edit.html", data)