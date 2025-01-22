from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User register with success!')
            return redirect('contact:index')

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
