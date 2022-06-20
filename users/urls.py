# Django
from django.urls import path

# Local
from . import views

app_name = "users"
urlpatterns = [
    path(
        route='login/', 
        view=views.LoginView.as_view(), 
        name='login'
    ),

    path(
        route='logout/', 
        view=views.LogoutView.as_view(), 
        name='logout'
    ),

    path(
        route='signup/', 
        view=views.SignUpView.as_view(), 
        name='signup'
    ),

    path(
        route='me/profile/', 
        view=views.ProfileUpdateView.as_view(), 
        name="update"
    ),

    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    )
]