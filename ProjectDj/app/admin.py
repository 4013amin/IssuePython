from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'created_time', 'updated_time', 'due_date']
    list_filter = ['status']
    search_fields = ['title']