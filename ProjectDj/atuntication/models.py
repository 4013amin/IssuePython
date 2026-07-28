from django.db import models

# Create your models here.
class Project(models.Model):
    file = models.FileField(upload_to='projects' , null = True, blank = True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.name