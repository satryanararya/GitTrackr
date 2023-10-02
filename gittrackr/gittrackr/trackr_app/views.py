from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class HomeView(ListView):
    template_name = "trackr_app/index.html"
    
    def get_queryset(self):
        return

class ProfileView(ListView):
    template_name = "trackr_app/profile.html"
    
    def get_queryset(self):
        return

class StatRepo(ListView):
    template_name = "trackr_app/stat.html"

    def get_queryset(self):
        return

class TailwindEx(ListView):
    template_name = "trackr_app/tailwindex.html"

    def get_queryset(self):
        return