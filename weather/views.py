from django.shortcuts import render
from .models import Weather
import json
import datetime

def showWeather(request):
    weathers = Weather.objects.all()
    x = []
    y_t = []
    y_p = []
    y_h = []
    w = []
    context = {'x' : [], 'y_t' : [], 'y_p' : [], 'y_h' : []}
    
    for weather in weathers:
        print(weather.weather_json)
        weather_info = json.loads(weather.weather_json)
        w.append({"x" : weather.time,
                  "y_t" : float(weather_info['temperature']),
                  "y_p" : float(weather_info['pressure']),
                  "y_h" : float(weather_info['humidity'])})
    
    w.sort(key=lambda d:d['x'])
    for _ in w:
        x.append(_['x'])
        y_t.append(_['y_t'])
        y_p.append(_['y_p'])
        y_h.append(_['y_h'])
    context['x'] = json.dumps(x)
    context['y_t'] = json.dumps(y_t)
    context['y_p'] = json.dumps(y_p)
    context['y_h'] = json.dumps(y_h)
    print(context)

    return render(request,'weather_data/weather.html',context=context)

