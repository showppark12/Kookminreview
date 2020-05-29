from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    #imge = models.ImageField(upload_to="blog/",blank=True,null=True) #media/blog/파일이름
    image = models.ImageField(upload_to="studyboard/",blank=True,null=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class StudyComment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Blog,on_delete=models.CASCADE)
    text = models.TextField()
    modify_date = models.DateTimeField(auto_now_add=True)