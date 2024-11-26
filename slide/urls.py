from django.urls import path
from . import views

app_name='slide'

urlpatterns = [
    path('', views.index, name='index'),
    path('change_text/', views.change_text, name='change_text'),
]
