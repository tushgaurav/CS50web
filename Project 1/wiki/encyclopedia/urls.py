from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entryview, name="viewentry"),
    path("random/", views.random, name="random"),
    path("submit/", views.submit, name="submit"),
    path("edit/", views.edit, name="edit"),
]
