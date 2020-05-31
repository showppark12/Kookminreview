from django.db import models
from django.contrib.auth.models import User

class BeerBoard(models.Model):
    title = models.CharField(max_length = 200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    img = models.ImageField(upload_to='beerboard/', blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.title

class BeerBoardComment(models.Model):
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    board = models.ForeignKey(BeerBoard, on_delete = models.CASCADE, related_name="comments")
    text = models.TextField()
    pub_date = models.DateTimeField()
