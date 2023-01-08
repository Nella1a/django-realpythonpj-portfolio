from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from projects.models import Project

def all_projects(request):
    # query the db to return all project objects
    projects = Project.objects.all()
    return render(request,"projects/all_projects.html", {'projects': projects})

