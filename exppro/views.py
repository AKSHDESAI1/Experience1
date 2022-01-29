from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def signup1(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login1')
        
        # return render(request, template_name='basic/signup.html', context=context)
    else:
        form = UserRegisterForm()
    return render(request, 'basic/signup.html', {'form': form})


def login1(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        context = {
            'form': form
        }
        if form.is_valid():

            return redirect('home')
        
        return render(request, template_name='account/login.html', context=context)
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, template_name='account/login.html', context=context)


def logout1(request):
    logout(request)
    return redirect('/')