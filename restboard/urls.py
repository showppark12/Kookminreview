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
    path('rcreate/<int:r_id>', views.ccreate, name= "rcreate"),
    path('rdelete_comment/<int:c_id>/<int:r_id>', views.delete_comment, name= "rdelete_comment"),

    # 스크랩
    path('<int:r_id>/rscrap', views.rscrap, name="rscrap"),
    path('<int:r_id>/rrscrap', views.rrscrap, name="rrscrap"),
]