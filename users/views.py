from django.shortcuts import render, redirect
from django.contrib import messages
#need to control what logged in users can do in system
from django.contrib.auth.decorators import login_required
#import the custom registration form we created with fields for email etc
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #save the user info use built in functionality
            form.save()
            #lets get the data from the form
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been successfully created! You are able to login below')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

#need to use the decorator to control access to the page
@login_required()
def profile(request):
    return render(request, 'users/profile.html')
