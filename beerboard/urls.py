from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blist, name="blist"),

    # 보드 CRUD 구현
    path('<int:b_id>', views.bdetail, name="bdetail"),
    path('create', views.bcreate, name="bcreate"),
    path('update/<int:b_id>', views.bupdate, name="bupdate"),
    path('delete/<int:b_id>', views.bdelete, name="bdelete"),
    path('ccreate/<int:b_id>', views.ccreate, name= "ccreate"),
    path('delete_comment/<int:c_id>', views.delete_comment, name= "delete_comment"),
]