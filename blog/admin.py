from django.contrib import admin

# Register your models here.
from blog.models import Posts
from blog.models import Category



class PostsAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)
