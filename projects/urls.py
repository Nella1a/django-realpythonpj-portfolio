from django.urls import path
from projects import views
from blog.urls import urlpatterns

app_name = "projects"
blog_entry = urlpatterns[0]
urlpatterns = [
    path("", views.all_projects, name="all_projects"),
    path("<int:pk>", views.project_detail, name="project_detail"),
]
