from django.contrib import admin

# Register your models here.
from .models import Posts
from .models import Category

admin.site.register(Posts)
admin.site.register(Category)