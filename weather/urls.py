from django.urls import path
from . import views

urlpatterns = [
    path('show_weather/',view=views.showWeather,name='show_weather'),
]
