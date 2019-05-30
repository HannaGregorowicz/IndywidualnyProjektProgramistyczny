from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
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

class MemberUpdate(UpdateView):
    model = Member
    fields = ['name', 'technologies', 'photo', 'more']

class MemberDelete(DeleteView):
    model = Member
    success_url = reverse_lazy('members:index')