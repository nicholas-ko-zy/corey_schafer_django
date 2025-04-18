from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Create a form that inherits from UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        # The model that is affected is the User model
        model = User
        # These are fields we want in the form, in this order
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    # A user update form to update the username and email
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    # A profile update form to update our profile picture
    class Meta: 
        model = Profile
        fields = ['image']