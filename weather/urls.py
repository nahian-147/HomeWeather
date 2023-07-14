from django.urls import path
from . import views

urlpatterns = [
    path('show_weather/',view=views.show_weather,name='show_weather'),
]
