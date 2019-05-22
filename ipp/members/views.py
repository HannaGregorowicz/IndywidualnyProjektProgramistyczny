from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Member

class IndexView(generic.ListView):
    template_name = 'members/index.html'
    context_object_name = 'all_members'

    def get_queryset(self):
        return Member.objects.all()

class DetailView(generic.DetailView):
    model = Member
    template_name = 'members/detail.html'

class MemberCreate(CreateView):
    model = Member
    fields = ['name', 'technologies', 'photo', 'more']