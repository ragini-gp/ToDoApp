from django.shortcuts import render, HttpResponse,redirect
# from home import models
from home.models import *
from home.forms import *

# Create your views here.
def index(request):
    tasks=Task.objects.all()

    form=TaskForm()

    if(request.method=="POST"):
        form=TaskForm(request.POST)
        if(form.is_valid):
            form.save()
        return redirect('/')
    context={
        'tasks':tasks,
        'form':form
    }
    return render(request,'list.html', context)

def update(request, primary_k):

    task=Task.objects.get(id=primary_k)
    form=TaskForm(instance=task)
    
    if(request.method=="POST"):
        form=TaskForm(request.POST,instance=task)

        if(form.is_valid):
            form.save()
        return redirect('/')
    context={
        'form':form
    }
    return render (request,'task_update.html',context)

def delete(request, primary_k):
    item=Task.objects.get(id=primary_k)

    if(request.method=="POST"):
        item.delete()
        return redirect('/')
    context={
        'item':item
    }
    return render(request,'delete.html',context)