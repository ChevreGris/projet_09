from . import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('flux')
        message = 'Identifiants invalides.'
    return render(request, 'authentication_app/login.html', context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')


def signup_page(request):
    form = forms.SigupForm()
    if request.method == 'POST':
        form = forms.SigupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('flux')
    return render(request, 'authentication_app/signup.html', context={'form': form})
