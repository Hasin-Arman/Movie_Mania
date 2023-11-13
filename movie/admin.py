from django.contrib import admin
from .models import movieModel,ReviewModel
# Register your models here.
admin.site.register(movieModel)
admin.site.register(ReviewModel)