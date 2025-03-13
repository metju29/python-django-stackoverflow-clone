from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import ProfileUpdateForm, UserUpdateForm


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

def profile_update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated successfully.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'stackusers/profile_update.html', context)
