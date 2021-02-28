from django.shortcuts import render
from django.http import HttpResponse
from events import models

# Create your views here.

def home(request):
    return render(request,'index.html')

def Destination(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        date = request.POST['date']
        time = request.POST['time']
        location = request.POST['location']
        image = request.POST['image']
        ins = models.EventData(event_name=event_name,date=date,time=time,location=location,image=image)
        ins.save()
        print("Written")
    return render(request,'events.html')

def Fetch(request):
    events = models.EventData.objects.all()
    return render(request, 'index.html', {'event':events})
