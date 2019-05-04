from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    photo = models.FileField(null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title