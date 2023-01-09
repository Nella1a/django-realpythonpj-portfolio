from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from projects.models import Project

def all_projects(request):
    # query the db to return all project objects
    projects = Project.objects.all()
    return render(request,"projects/all_projects.html", {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html', {'project': project})