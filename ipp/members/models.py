from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=200)
    technologies = models.CharField(max_length=500)
    photo = models.FileField()
    more = models.TextField()

    def __str__(self):
        return self.name
