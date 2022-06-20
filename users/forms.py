# Django
from django import forms

# Local
from .models import User, Profile


class SignupForm(forms.Form):
    """Sign up form."""
    username = forms.CharField(min_length=4, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput
    )

    password = forms.CharField(
        min_length=8, 
        max_length=70, 
        widget=forms.PasswordInput
    )

    password_confirmation = forms.CharField(
        min_length=8, 
        max_length=70, 
        widget=forms.PasswordInput
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('Username is already in use.')

        return username
    
    def clean_email(self):
        """Email must be unique."""
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()

        if email_taken:
            raise forms.ValidationError('Email is already in use.')

        return email
    
    def clean(self):
        """Verifies password confirmation."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        
        return data
    
    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        Profile.objects.create(user=user)