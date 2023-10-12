from django.shortcuts import render
from .models import City, Vacancies
def home(request):
    city = City.objects.all()
    vacancies = Vacancies.objects.all()
    return render(request,'EtalonSite/home.html',{'city':city,"vacancies":vacancies})