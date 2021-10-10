from django.db import models

# Create your models here.
from django.urls import reverse


class Event(models.Model):
    name = models.CharField(max_length=200)
    when = models.DateTimeField()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('eventapp:event-detail', kwargs={'pk': self.pk})
