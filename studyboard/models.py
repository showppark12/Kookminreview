from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(upload_to="studyboard/",blank=True,null=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    sscrap_users = models.ManyToManyField(User, related_name="sscraps")

    def __str__(self):
        return self.title

class StudyComment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Blog,on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    modify_date = models.DateTimeField(auto_now_add=True)