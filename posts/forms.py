# Django
from django import forms

# Local
from .models import Post


class PostForm(forms.ModelForm):
    """Post model."""
    class Meta:
        """Form settings."""
        model = Post
        fields = ('user', 'profile', 'title', 'photo')