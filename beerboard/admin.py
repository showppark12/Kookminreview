from django.contrib import admin
from .models import BeerBoard
from .models import BeerBoardComment

# Register your models here.
admin.site.register(BeerBoard)
admin.site.register(BeerBoardComment)
