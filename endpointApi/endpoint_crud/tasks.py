from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.utils import timezone
from endpoint_crud.models import Endpoint
from datetime import datetime, timedelta


@shared_task(name = "delete_older_endpoints")
def delete_older_endpoints(*args, **kwargs):
  now = timezone.now()
  before = now - timedelta(hours=1)
  endpoints = Endpoint.objects.filter(created__lt=before)
  endpoints.delete()
