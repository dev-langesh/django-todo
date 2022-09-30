from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import TodoForm
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

from .models import Todo

def loginUser(request):

   if request.user.is_authenticated :
        return redirect('home')

   if request.method == 'POST':
    username = request.POST.get("username")
    password = request.POST.get('password')

    try:
        user = User.objects.get(username = username)
    except :
        messages.error(request,"User not found")

    user = authenticate(request,username=username,password=password)

    if user is not None:
        login(request,user)
        return redirect('home')

    else :
        messages.error(request,"Invalid credentials")

   return render(request,'base/login.html')

def logoutUser(request):
    logout(request)
    return redirect("home")

def getTodos(request):

    data = Todo.objects.all()

    context = {'todos' : data}

    return render(request,'base/home.html',context)

@login_required(login_url='login')
def createTodo(request):

    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form' : form}

    return render(request,'base/create.html',context)

@login_required(login_url='login')
def editTodo(request,pk):
    todo = Todo.objects.get(id=pk)

    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}

    return render(request,'base/create.html',context)

@login_required(login_url='login')
def deleteTodo(request,pk):
    todo = Todo.objects.get(id=pk)

    context = {'todo':todo}

    if request.method == 'POST':
        todo.delete()
        return redirect('home')

    return render(request,'base/delete.html',context)


