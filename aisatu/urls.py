from django.urls import path
from . import views

app_name = 'aisatu'

urlpatterns = [
    path('',views.IndexView.as_view(),name="top")
]

