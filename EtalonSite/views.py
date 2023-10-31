from django.shortcuts import render
from .models import City, Vacancies,Contacts,Telegram,File


def home(request):
    city = City.objects.all()
    vacancies = Vacancies.objects.all()
    return render(request,'EtalonSite/home.html',{'city':city,"vacancies":vacancies})

def vacancies(request):
    vacancies = Vacancies.objects.all()
    return render(request,'EtalonSite/vacancies.html',{"vacancies":vacancies})

def contacts(request):
    contacts = Contacts.objects.first()
    telegram = Telegram.objects.all()
    return render(request,'EtalonSite/contacts.html',{'contacts':contacts,'telegram':telegram})

def files(request):
    files = File.objects.all()
    return render(request,'EtalonSite/files.html',{'files':files})