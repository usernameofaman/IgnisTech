from django.db import models

# Create your models here.
class EventData(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    location = models.CharField(max_length=100,default='LOCATION')
    is_liked = models.BooleanField(default=False)
    image = models.FileField(blank=True)
     

    

    