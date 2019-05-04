from django.http import Http404
from django.shortcuts import render
from .models import Project

def index(request):
    all_projects = Project.objects.all()        #takes all projects from database
    context = {
        'all_projects': all_projects,
    }
    return render(request, 'projects/index.html', context)

def detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Nie ma takiego projektu :(")
    return render(request, 'projects/detail.html', {'project': project})
