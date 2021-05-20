from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Endpoint(models.Model):
    endpoint_suffix = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

class EndpointActivity(models.Model):
    endpoint = models.ForeignKey(Endpoint, on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
    headers = models.TextField()


