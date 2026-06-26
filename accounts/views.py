from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from .forms import RegisterForm


def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                'Account created successfully.'
            )

            return redirect('home')

    else:

        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def logout_view(request):

    logout(request)

    messages.success(
        request,
        'Logged out successfully.'
    )

    return redirect('home')
