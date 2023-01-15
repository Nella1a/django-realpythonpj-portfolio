from django.urls import path
from .views import blog_index
from .views import blog_detail
from .views import blog_category

app_name = "blog"

urlpatterns = [
    path("", blog_index, name="all_posts"),
    path("<int:pk>/", blog_detail, name="blog_detail"),
    path("<category>/", blog_category, name="blog_category")
]
