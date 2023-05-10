from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def _login(request):
    if request.method == 'GET':
        return render(request, 'html/registration/login.html')
    elif request.method == 'POST':
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Обработка ошибки логина
            return render(request, 'html/registration/login.html', {'error': 'Неверное имя пользователя или пароль'})


def _register(request):
    if request.method == 'GET':
        return render(request, 'html/registration/register.html')
    elif request.method == 'POST':
        username, password = request.POST['username'], request.POST['password']
        print(password)
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Обработка ошибки логина
            return render(request, 'html/registration/register.html', {'error': 'Неверное имя пользователя или пароль'})
