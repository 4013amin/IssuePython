from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    re_path(r'^$', index, name='index'),
    re_path(r'^(?!api/|admin/).*$', index, name='catch-all'),
]
