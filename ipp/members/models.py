from django.db import models
from django.core.urlresolvers import reverse

class Member(models.Model):
    name = models.CharField(max_length=200)
    technologies = models.CharField(max_length=500)
    photo = models.FileField()
    more = models.TextField()

    def get_absolute_url(self):
        return reverse('members:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
