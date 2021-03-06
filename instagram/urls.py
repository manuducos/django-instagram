# Django
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

# Local
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='', 
        view=views.index,
        name='index'
    ),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)