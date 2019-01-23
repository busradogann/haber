from django.urls import path
from . import views

urlpatterns = [
    path('', views.haber, name='haber'),
]