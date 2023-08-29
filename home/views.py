from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import User
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = UserRegister()
    users = User.objects.all()
    context = {
        'form': form,
        'users': users,
    }
    return render(request, 'home/index.html', context)

def update(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        form = UserRegister(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        user = User.objects.get(id=id)
        form = UserRegister(instance=user)
    context = {
        'form': form,
    }
    return render(request, 'home/update.html', context)

def delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.delete()
    return redirect('index')

