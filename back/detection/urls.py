from django.urls import path
from . import views

urlpatterns = [
    path('', views.detection),
    path('detect/', views.detect, name='send_file'),

]