from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FoodBoard(models.Model):
    title = models.CharField(max_length = 200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    img = models.ImageField(upload_to='foodboard/', blank=True, null=True)
    text = models.TextField()
    #recommend = models.IntegerField()
    #reply ???

    def __str__(self):
        return self.title
    
    def summary(self):
        if len(self.text)>100: return self.text[:100] + "..."
        return self.text