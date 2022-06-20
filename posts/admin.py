# Django
from django.contrib import admin

# Local
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'user', 'profile', 
        'title', 'photo', 'created', 
        'modified'
    )
    list_display_links = ('pk', 'user', 'profile')
    list_editable = ('title',)

    search_fields = (
        'user',
        'profile',
        'title'
    )

    list_filter = ('created', 'modified')

    fieldsets = (
        ('User/Profile', {
            'fields': (
                ('user', 'profile'),
            )
        }),
        ('Post', {
            'fields': (
                ('title',),
                ('photo',)
            )
        }),
        ('Metadata', {
            'fields': (
                ('pk', 'created', 'modified')
            ),
        })
    )

    readonly_fields = ('pk', 'created', 'modified')