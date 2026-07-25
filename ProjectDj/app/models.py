from tabnanny import verbose

from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    status = models.BooleanField(default=False, verbose_name="وضعیت")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="زمان بروزرسانی")
    due_date = models.DateTimeField(null=True, blank=True, verbose_name="تاریخ سررسید")

    def __str__(self):
        return self.title