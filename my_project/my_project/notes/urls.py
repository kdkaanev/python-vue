
from django.urls import include, path
from rest_framework import routers
from my_project.notes import views

urlpatterns = (
    path('notes/', views.notes),
    path('note/<int:pk>/', views.note_detail),
)