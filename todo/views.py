from multiprocessing import context
from turtle import title
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def home(request):
    tasks = Todo.objects.filter(user_id=request.user.id)
    form = TodoForm()

    if request.method == 'GET':
        searcher = request.GET.get('searcher') or ''
        if searcher:
            tasks = Todo.objects.filter(user_id=request.user.id, title__icontains=searcher)
    context = {
        'tasks':tasks,
        'form':form,
       # 'searcher':searcher
    }
    return render(request, 'todo/home.html', context)

@login_required(login_url='/login/')
def createFormView(request):
    form = TodoForm()

    # lets capture the post which is coming from create.html
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect('/')
    context = {
        'form':form
    }
    return render(request, 'todo/create.html', context)

@login_required(login_url='/login/')
def update(request, pk):
    task =  Todo.objects.get(id=pk)
    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.instance.user = request.user
            form.save()

    context = {
        'task':task,
        'form':form
    }
    return render(request, 'todo/update.html', context)

@login_required(login_url='/login/')
def delete(request, pk):
    task =  Todo.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {
        'task':task,
    }
    return render(request, 'todo/delete.html', context)

def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'user':form
    }
    return render(request, 'todo/signup.html', context)

def loginView(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    context = {
        'form':form
    }
    return render(request, 'todo/login.html', context)

@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')