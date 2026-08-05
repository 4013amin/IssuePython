from django.urls import path

from . import views


urlpatterns = [
    path('add_product/' , views.AddToCartView.as_view()),
]