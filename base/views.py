from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Todo

def createTodo(request):

    data = Todo.objects.all()

    context = {'todos' : data}

    return render(request,'base/home.html',context)
