from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import user_passes_test, login_required


def not_logged_in(user):
    return not user.is_authenticated

@user_passes_test(not_logged_in, login_url='stackbase:home')
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Acount successfully created for {username}! Log in now')
            return redirect('login')
    else:
        form = UserRegisterForm()
 
    return render(request, 'stackusers/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'stackusers/profile.html')
