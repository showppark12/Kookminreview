from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="food_home"),

    # 보드 CRUD 구현
    path('<int:review_id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('edit/<int:review_id>', views.edit, name="edit"),
    path('delete/<int:review_id>', views.delete, name="delete"),

    # 덧글 CRUD 구현
    path('<int:review_id>/c<int:comment_id>', views.new_comment, name="new_comment"),
    path('edit/c<int:comment_id>', views.edit_comment, name="edit_comment"),
    path('delete/c<int:comment_id>', views.delete_comment, name="delete_comment"),
] 