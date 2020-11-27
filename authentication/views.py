from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserCreateForm, UserEditForm
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_listener = True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = UserCreateForm()
    context = {
       'form': form
    }
    return render(request, 'register.html', context)


def edit_user(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_listener = True
            user.save()
            return redirect('home')
    else:
        form = UserCreateForm(instance=request.user)
    context = {
       'form': form
    }
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        credential = authenticate(request, username=email, password=password)
        if credential is not None:
            user = CustomUser.objects.get(email=email)
            if user.is_authenticated:
                login(request, credential)
                return redirect('home')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def change_password(request):
    if request.method == 'True':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
    else:
        form = PasswordChangeForm()
    context = {
        'form': form
    }
    return render(request, 'change_password.html', context)
