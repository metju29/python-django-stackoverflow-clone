from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Acount successfully created for {username}! Log in now')
            return redirect('stackbase:home')
    else:
        form = UserRegisterForm()

    return render(request, 'stackusers/register.html', {'form': form})

