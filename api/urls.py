from django.urls import path
from . import views

urlpatterns = [
    path('save_weather/',view=views.save_weather,name='save_weather'),
    path('all_weather/',view=views.get_all_weather,name='all_weather'),
    path('ranged_weather/',view=views.get_weather_from_t1_to_t2,name='ranged_weather'),
    path('last_t_seconds/',view=views.get_weather_last_t_seconds,name='last_t_seconds'),
]
