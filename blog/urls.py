from django.urls import path
from .views import blog_index

app_name = " blog"

urlpatterns = [
    path("", blog_index, name="all_posts")
]
