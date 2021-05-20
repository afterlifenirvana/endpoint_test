import json
from datetime import timedelta

from django.utils import timezone
from rest_framework import serializers

from endpoint_crud.models import Endpoint, EndpointActivity


class EndpointSerializer(serializers.ModelSerializer):
    hits = serializers.SerializerMethodField()

    class Meta:
        model = Endpoint
        fields = '__all__'

    def get_hits(self, instance):
        now = timezone.now()
        before = now - timedelta(minutes=5)
        return EndpointActivity.objects.filter(endpoint=instance, created__range=(before, now)).count()


class EndpointActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EndpointActivity
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['data'] = json.loads(ret['data'])
        ret['headers'] = json.loads(ret['headers'])
        return ret
