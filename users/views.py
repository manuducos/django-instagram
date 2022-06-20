# Django
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.views.generic import DetailView, FormView, UpdateView

# Local
from .forms import SignupForm
from posts.models import Post
from .models import Profile


class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "users/update_profile.html"
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile
    
    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class SignUpView(FormView):
    """Users sign up view."""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('posts:feed')
    
    def form_valid(self, form):
        """Save form data."""
        form.save()

        username = form['username'].value()
        password = form['password'].value()

        user = authenticate(
            self.request, 
            username=username, 
            password=password
        )

        login(self.request, user)

        return super().form_valid(form)


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/logout.html'