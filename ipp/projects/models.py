from django.db import models
from django.core.urlresolvers import reverse

class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=800)
    photo = models.FileField(null=True)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title