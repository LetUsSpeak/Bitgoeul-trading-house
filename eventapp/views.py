from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from eventapp.models import Event


class EventList(ListView):
    model = Event
    template_name = 'eventapp/main.html'

class EventDetail(DetailView):
    model = Event
    template_name = 'eventapp/countdown.html'