from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import TodoForm

# Create your views here.

from .models import Todo

def getTodos(request):

    data = Todo.objects.all()

    context = {'todos' : data}

    return render(request,'base/home.html',context)

def createTodo(request):

    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form' : form}

    return render(request,'base/create.html',context)
