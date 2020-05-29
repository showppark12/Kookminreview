from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:review_id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('edit/<int:review_id>', views.edit, name="edit"),
    path('delete/<int:review_id>', views.delete, name="delete"),
] 