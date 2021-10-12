from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from eventapp.forms import EventCreationForm
from eventapp.models import Event


class EventList(ListView):
    model = Event
    template_name = 'eventapp/main.html'

class EventDetail(DetailView):
    model = Event
    template_name = 'eventapp/countdown.html'

class EventCreateView(CreateView):
    model = Event
    form_class = EventCreationForm
    template_name = 'eventapp/create.html'

    def get_success_url(self):
        return reverse('eventapp:event-list')
