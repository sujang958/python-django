from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'description')

admin.site.register(Post, PostAdmin)