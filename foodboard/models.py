from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FoodBoard(models.Model):
    title = models.CharField(max_length = 200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    img = models.ImageField(upload_to='foodboard/', blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.title


class FoodComment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(FoodBoard, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    modify_date = models.DateTimeField(auto_now_add=True)