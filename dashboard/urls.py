from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('scan', views.scan, name='scan'),
]
