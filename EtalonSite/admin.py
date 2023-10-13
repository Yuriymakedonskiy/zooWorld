from django.contrib import admin
from .models import City,Vacancies,Contacts,Telegram

admin.site.register(City)
admin.site.register(Vacancies)
admin.site.register(Contacts)
admin.site.register(Telegram)