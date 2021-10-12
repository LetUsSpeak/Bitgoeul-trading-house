from django.contrib.auth.models import User
from django.db import models

# Create your models here.\

from productapp.models import Product


class Review(models.Model):

    content = models.TextField(null=False)

    sentiment = models.IntegerField(null=True)
