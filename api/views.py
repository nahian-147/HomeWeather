from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from weather.serializers import WeatherSerializer
from weather.models import Weather
import json
import time

@api_view(['POST'])
def saveWeather(request):
    
    weather = request.data
    weatherRecord = Weather()
    weatherRecord.weather_json = json.dumps(weather['weather_json'])
    weatherRecord.time = float(weather['time'])
    try:
        weatherRecord.save()
        return Response({'message' : 'saved'}, status=201)
    except:
        return Response({'message' : 'bad format'}, status=501)


@api_view(['GET'])
def getAllWeather(request):
    allWeatherSerialized = WeatherSerializer(Weather.objects.all(), many=True)
    return Response(allWeatherSerialized.data, status=200)


@api_view(['GET'])
def get_weather_from_t1_to_t2(request):
    t1 = request.GET.get('t1')
    t2 = request.GET.get('t2')
    weather_from_t1_to_t2 = WeatherSerializer(Weather.objects.filter(time__range=(t1, t2)), many=True)
    return Response(weather_from_t1_to_t2.data, status=200)

@api_view(['GET'])
def get_weather_last_t_seconds(request):
    t = float(request.GET.get('t'))
    weather_last_t_seconds = WeatherSerializer(Weather.objects.filter(time__range=(time.time()-t, time.time())), many=True)
    return Response(weather_last_t_seconds.data, status=200)