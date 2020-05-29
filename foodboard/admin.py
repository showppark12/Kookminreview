from django.contrib import admin
from .models import FoodBoard, FoodComment

# Register your models here.
admin.site.register(FoodBoard)
admin.site.register(FoodComment)