from django.contrib import admin

# Register your models here.
from eventapp.models import Event

admin.site.register(Event)