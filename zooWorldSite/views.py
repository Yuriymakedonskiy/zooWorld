from django.shortcuts import render
from .models import *

def home(request):
    ratings = Rating.objects.all()
    if request.method == "POST":
        print("__NEW__")
        rating = Rating(
            score=request.POST.get("val"),
            name=request.POST.get("name"),
            review=request.POST.get("review"),
        )
        print(rating.score)
        rating.save()
    return render(request,'zooWorldSite/home.html',{"ratings": ratings})
def animal(request):
    return render(request,'zooWorldSite/animal.html')
def ticket(request):
    return render(request,'zooWorldSite/ticket.html')
