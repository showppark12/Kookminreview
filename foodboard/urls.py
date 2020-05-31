from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.FBoardHome, name="food_home"),

    # 보드 CRUD 구현
    path('<int:review_id>', views.FBoardDetail, name="FBoardDetail"),
    path('FBoardNew/', views.FBoardNew, name="FBoardNew"),
    path('FBoardEdit/<int:review_id>', views.FBoardEdit, name="FBoardEdit"),
    path('FBoardDelete/<int:review_id>', views.FBoardDelete, name="FBoardDelete"),
    path('<int:review_id>/FNewComment', views.new_comment, name= "FNewComment"),
    path('FDelComment/<int:comment_id>', views.delete_comment, name= "FDelComment"),
    path('FEditComment/<int:comment_id>', views.delete_comment, name= "FEditComment"),
    
    # 덧글 CRUD 구현
    #path('<int:review_id>/c<int:comment_id>', views.new_comment, name="new_comment"),
    #path('delete/c<int:comment_id>', views.delete_comment, name="delete_comment"),
] 