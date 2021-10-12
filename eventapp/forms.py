from django.forms import ModelForm

from eventapp.models import Event


class EventCreationForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'when', 'info', 'market_image']