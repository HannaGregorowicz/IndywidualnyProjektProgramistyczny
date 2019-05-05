from django.shortcuts import render, get_object_or_404
from .models import Project

def index(request):
    all_projects = Project.objects.all()        #takes all projects from database
    context = {
        'all_projects': all_projects,
    }
    return render(request, 'projects/index.html', context)

def detail(request, project_id):
    # project = Project.objects.get(pk=project_id)
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': project})
