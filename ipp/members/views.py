from django.http import Http404
from django.shortcuts import render
from .models import Member

def index(request):
    all_members = Member.objects.all()  # takes all projects from database
    context = {
        'all_members': all_members,
    }
    return render(request, 'members/index.html', context)

def detail(request, member_id):
    try:
        member = Member.objects.get(pk=member_id)
    except Member.DoesNotExist:
        raise Http404("Nie ma takiego członka :(")
    return render(request, 'members/detail.html', {'member': member})
