from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from todolist_app.models import todo
from django.http import HttpResponseRedirect
from todolist_app import models

# Create your views here.
def home(request):
    
    todo_items=todo.objects.all().order_by('-added_date')
    return render(request,'my_app/index.html',{"todo_items":todo_items})


@csrf_exempt
def add_todo(request):
    
    currentdate=timezone.now()
    content=request.POST['content']
    created_object=todo.objects.create(added_date=currentdate,text=content)
    return HttpResponseRedirect('/')


@csrf_exempt
def delete_todo(request,todo_id):
    todo.objects.get(id=todo_id).delete()   
    return HttpResponseRedirect('/')
        