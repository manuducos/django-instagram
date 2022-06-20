# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# Local
from .forms import PostForm
from .models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
	"""Returns all published posts."""
	template_name = 'posts/feed.html'
	model = Post
	ordering = ('-created')
	paginate_by = 10
	context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
	"""Returns the detail of a post."""
	template_name = 'posts/detail.html'
	slug_field = 'pk'
	slug_url_kwarg = 'id'
	queryset = Post.objects.all()
	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		post = self.get_object()
		context['post'] = Post.objects.get(pk=post.pk)
		return context


class CreatePostView(LoginRequiredMixin, CreateView):
	"""Create a new post."""
	template_name = 'posts/new.html'
	form_class = PostForm
	success_url = reverse_lazy('posts:feed')

	def get_context_data(self, **kwargs):
		"""Add user and profile to context."""
		context = super().get_context_data(**kwargs)
		context['user'] = self.request.user
		context['profile'] = self.request.user.profile
		return context