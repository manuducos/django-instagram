# Django
from django.shortcuts import redirect


def index(request):
    """Index view. Redirects to feed."""
    return redirect('posts:feed')