from django.db import models
from django.db.models.base import Model

class Weather(models.Model):
    weather_json = models.JSONField()
    time = models.FloatField(primary_key=True)
    
    def __str__(self):
        return str(self.time)
