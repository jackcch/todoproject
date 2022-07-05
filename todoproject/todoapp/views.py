from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import get_object_or_404
from .models import todomodel
from .forms import TodoForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect('currenttodo')
    else:
        return render(request, 'todoapp/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todoapp/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodo')
            except IntegrityError:
                return render(request, 'todoapp/signupuser.html', {'form':UserCreationForm(),'errmsg':'User ID is unavailable'})
        else:
            return render(request, 'todoapp/signupuser.html', {'form':UserCreationForm(),'errmsg':'Password Mismatched'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todoapp/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user == None:
            return render(request, 'todoapp/loginuser.html', {'form':AuthenticationForm(), 'errmsg':'Invalid User ID or Password'})
        else:
            login(request, user)
            return redirect('currenttodo')

@login_required
def logoutuser(request):
    logout(request)
    return redirect('home')

@login_required
def currenttodo(request):
    todos = todomodel.objects.filter(author=request.user, completed__isnull = True)
    return render(request, 'todoapp/currenttodo.html',{'todos':todos})

@login_required
def completedtodo(request):
    todos = todomodel.objects.filter(author=request.user, completed__isnull = False)
    return render(request, 'todoapp/completedtodo.html',{'todos':todos})

@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todoapp/createtodo.html',{'form':TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.author = request.user
            newtodo.save()
            return redirect('currenttodo')
        except ValueError:

             return render(request, 'todoapp/createtodo.html',{'form':TodoForm(),'errmsg':'Bad User Input'})

@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(todomodel, pk=todo_pk, author=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todoapp/viewtodo.html',{'todo':todo, 'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request, 'todoapp/viewtodo.html',{'form':form,'errmsg':'Bad User Input'})

@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(todomodel, pk=todo_pk, author=request.user)
    todo.delete()
    return redirect('currenttodo')

@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(todomodel, pk=todo_pk, author=request.user)
    if request.method == 'POST':
        todo.completed = timezone.now()
        todo.save()
        return redirect('currenttodo')
