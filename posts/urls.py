# Django
from django.urls import path

# Local
from . import views

app_name = "posts"
urlpatterns = [
    path(
        route='', 
        view=views.PostsFeedView.as_view(), 
        name='feed'
    ),

    path(
        route='new/', 
        view=views.CreatePostView.as_view(), 
        name="create_post"
    ),

    path(
        route='<int:id>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    )
]