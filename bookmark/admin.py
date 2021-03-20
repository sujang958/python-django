from django.contrib import admin
from bookmark.models import *

class BookMarKAdmin(admin.ModelAdmin):
    list_display = ('id', "title", 'url');

admin.site.register(Bookmark, BookMarKAdmin);