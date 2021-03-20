from django.shortcuts import render
from django.views.generic import *
from bookmark.models import Bookmark


class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark