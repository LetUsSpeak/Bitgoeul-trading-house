from django.forms import ModelForm, forms

from eventapp.models import Event


class EventCreationForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'when', 'info', 'market_image']

        # when = forms.DateTimeField(widget=forms.DateTimeField(attrs={'placeholder': '2021-10-12 18:00:00'}))