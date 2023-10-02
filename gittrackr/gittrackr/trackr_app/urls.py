from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("profile",views.ProfileView.as_view(), name="Profile"),
    path("stat",views.StatRepo.as_view(), name="StatRepo"),
    path("tailwind", views.TailwindEx.as_view(), name="tailwind"),
]