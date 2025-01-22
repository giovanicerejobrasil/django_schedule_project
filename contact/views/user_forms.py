from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User register with success!')
            return redirect('contact:login')

        return render(
            request,
            'contact/register.html',
            {'form': form}
        )

    return render(
        request,
        'contact/register.html',
        {'form': form}
    )


def login(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Logged with success')
            auth.login(request, user)

            return redirect('contact:index')

        messages.error(request, 'Invalid login')

    return render(
        request,
        'contact/login.html',
        {'form': form}
    )


def logout(request):
    auth.logout(request)

    return redirect('contact:login')
