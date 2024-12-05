from django.shortcuts import render
from .models import User,Post
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = "blog/base.html"



