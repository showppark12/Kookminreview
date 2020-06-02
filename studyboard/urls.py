import studyboard.views
from django.conf import settings
from django.urls import path,include

urlpatterns = [    
    path('',studyboard.views.home, name ="studyboardhome"),
    path('new/',studyboard.views.new, name = "studyboardnew"),
    path('create/',studyboard.views.create,name="studyboardcreate"),
    path('edit/<int:blog_id>',studyboard.views.edit,name="studyboardedit"),
    path('update/<int:blog_id>',studyboard.views.update,name ="studyboardupdate"),
    path('delete/<int:blog_id>',studyboard.views.delete,name ="studyboarddelete"),
    path('<int:blog_id>/scrap',studyboard.views.scrap, name = "studyboardscrap"),
    path('<int:blog_id>/rscrap',studyboard.views.rscrap, name = "studyboardrscrap"),
    path('<int:blog_id>',studyboard.views.detail, name = "studyboarddetail"),
    path('sdelete_comment/<int:c_id>', studyboard.views.sdelete_comment, name= "sdelete_comment"),
    path('sccreate/<int:b_id>', studyboard.views.sccreate, name= "sccreate"),
]