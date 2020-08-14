from django.shortcuts import render
from django.http import HttpResponse
from .models import xplore

# Create your views here.
def index(request):
    x = xplore.objects.all
    return render(request, 'login.html', {"xplore": x})

def register(request):
    if request.method=="POST":
        username = request.POST.get("user","")
        mailID = request.POST.get("mail","")
        location = request.POST.get("loc","")

        explore = xplore(user=username,mail=mailID,loc=location)
        explore.save()
    return render(request, 'login.html')