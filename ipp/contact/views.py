from .models import PointOfInterest
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'contact/index.html'
    context_object_name = 'all_points'

    def get_queryset(self):
        return PointOfInterest.objects.all()