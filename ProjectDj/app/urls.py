from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, index

router = DefaultRouter()
router.register('todos', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
