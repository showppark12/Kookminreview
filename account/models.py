from django.db import models
from django.contrib.auth.models import AbstractUser


# # Create your models here.
# class User(AbstractUser):
#     GENDER = (
#         ("M", "남자"),
#         ("W", "여자"),
#     )

#     date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
#     profile = models.TextField()
#     profile_img = models.ImageField(upload_to='account/', blank=True, null=True)
#     gender = models.CharField(max_length=100, blank=True, null=True, choices=GENDER)