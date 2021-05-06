from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = 'home/home.html'
