from django.db import models

class City(models.Model):
    title = models.CharField(max_length=100)
    titleEN = models.CharField(max_length=100)
    def __str__(self):
        return self.title
     
class Vacancies(models.Model):
    title = models.CharField(max_length=100)
    workExperience = models.CharField(max_length=50)
    salary = models.CharField(max_length=30)
    requirements = models.CharField(max_length=300)
    responsibilities = models.CharField(max_length=200)
    conditions = models.CharField(max_length=200)
    def __str__(self):
        return self.title 
    
class Contacts(models.Model):
    TIN = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.email
    
class Telegram(models.Model):
    idTelegram = models.CharField(max_length=60)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.idTelegram