import uuid
import json

from django.shortcuts import render
import urllib.parse
from django.utils import timezone
from datetime import timedelta
from rest_framework import viewsets, views, status

from endpoint_crud.serializers import EndpointSerializer, EndpointActivitySerializer
from endpoint_crud.models import Endpoint, EndpointActivity

# Create your views here.
from rest_framework.response import Response


class EndpointViewSet(viewsets.ModelViewSet):
    serializer_class = EndpointSerializer
    authentication_classes = ()

    def get_queryset(self):
        now = timezone.now()
        before = now - timedelta(hours=1)
        return Endpoint.objects.filter(created__range=(before, now))

    def create(self, request, *args, **kwargs):
        # if 'endpoint_suffix' in request.data and request.data.get('endpoint_suffix', '') != '':
        request.data['endpoint_suffix'] = uuid.uuid4().hex[:25].upper()
        #     endpoint = request.data.get('endpoint_suffix')
        #     request.data['endpoint_suffix'] = urllib.parse.urljoin(request.build_absolute_uri('/'), endpoint)
        return super(EndpointViewSet, self).create(request, *args, **kwargs)
        # else:
        #     return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        obj_id = kwargs.get('pk', '')
        if obj_id:
           try:
            endpoint = Endpoint.objects.get(pk=obj_id)
            serializer = self.get_serializer(endpoint)
            endpoint_act = EndpointActivity.objects.filter(endpoint=endpoint)
            activity_serializer = EndpointActivitySerializer(endpoint_act, many=True)
            data = {
                'endpoint': serializer.data,
                'endpoint_activity': activity_serializer.data,
                'base_url': request.build_absolute_uri('/')
            }
            return Response(data, status=status.HTTP_200_OK)
           except Endpoint.DoesNotExist:
               return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class EndpointActivityViewSet(views.APIView):
    authentication_classes = ()

    def add_activity(self, request, url):
        try:
            endpoint = Endpoint.objects.get(endpoint_suffix=url)
            data = {
                'data': request.data,
                'query_params': request.query_params,
                'method': request.method
            }
            headers = {x: request.headers[x] for x in request.headers}
            activity = {
                'endpoint': endpoint.id,
                'data': json.dumps(data),
                'headers': json.dumps(headers)
            }
            serializer = EndpointActivitySerializer(data=activity)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Endpoint.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        print('here')
        url = kwargs.get('url', '')
        if url:
            return self.add_activity(request, url)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        url = kwargs.get('url', '')
        if url:
            return self.add_activity(request, url)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        url = kwargs.get('url', '')
        if url:
            return self.add_activity(request, url)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        url = kwargs.get('url', '')
        if url:
            return self.add_activity(request, url)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        url = kwargs.get('url', '')
        if url:
            return self.add_activity(request, url)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
