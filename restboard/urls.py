from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.rlist, name="rlist"),

    # 보드 CRUD 구현
    path('<int:r_id>', views.rdetail, name="rdetail"),
    path('create', views.rcreate, name="rcreate"),
    path('update/<int:r_id>', views.rupdate, name="rupdate"),
    path('delete/<int:r_id>', views.rdelete, name="rdelete"),
    # path('ccreate/<int:r_id>', views.ccreate, name= "ccreate"),
]