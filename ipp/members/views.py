from django.shortcuts import render, get_object_or_404
from .models import Member

def index(request):
    all_members = Member.objects.all()  # takes all projects from database
    context = {
        'all_members': all_members,
    }
    return render(request, 'members/index.html', context)

def detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'members/detail.html', {'member': member})
