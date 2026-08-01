from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Project(models.Model):
    file = models.FileField(upload_to='projects' , null = True, blank = True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null = True, blank = True)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='auth_profile')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    phone = models.IntegerField()
    bio = models.TextField()
    def __str__(self):
        return self.user.username

class Posts(models.Model):
    name = models.CharField(max_length=150 , verbose_name="نام")
    des = models.CharField(max_length=150 , verbose_name="توضیحات")
    like = models.IntegerField(default=0 , verbose_name="لایک ها")
    comments = models.TextField(verbose_name="کامنت ها")

    def __str__(self):
        return Posts.name