from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Project

class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return Project.objects.all()

class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

class ProjectCreate(CreateView):
    model = Project
    fields = ['title', 'description', 'photo']

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['title', 'description', 'photo']

class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:index')



"""
----- To jest poprzednia wersja -----

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
"""

