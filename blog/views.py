from django.shortcuts import render
from django.views.generic import *
import blog.models as blogModels

class BlogLV(ListView):
    model = blogModels.Post