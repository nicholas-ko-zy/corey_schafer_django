from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    # Add in conditional to handle a POST request, to validate the form data
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Save a user
            form.save()
            # Form passes validation check, get the username and return a message.
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            # After a successful sign-up, use redirect function to
            # send the user back to the homepage.   
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Create user's profile view

@login_required
def profile(request):
    # Add requirement for user to be logged in to see profile
    return render(request, 'users/profile.html')


# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error