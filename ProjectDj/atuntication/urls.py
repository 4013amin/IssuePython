from django.urls import path
from . import views

urlpatterns = [
    path('projects/' , views.ProjectDashboard.as_view()),
    path('projects/<int:pk>/', views.ProjectDashboard.as_view(), name='project-update'),

]