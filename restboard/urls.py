from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:restboard_id>', views.detail, name = "detail"),
    path('new',views.new, name="new"),
    path('create',views.create, name = "create"),
    path('edit/<int:restboard_id>',views.edit, name = "edit"),
    path('update/<int:restboard_id>',views.update, name = "update"),
    path('delete/<int:restboard_id>',views.delete, name = "delete"),
]