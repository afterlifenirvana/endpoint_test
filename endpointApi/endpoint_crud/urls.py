from django.conf import settings
from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from endpoint_crud.views import EndpointViewSet

from endpoint_crud.views import EndpointActivityViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


urlpatterns = [
    path("endpoint/<int:pk>/", EndpointViewSet.as_view({'get': 'retrieve'}), name='endpoint-detail'),
    url(r"endpoint/$", EndpointViewSet.as_view({'get': 'list', 'post': 'create'}), name='endpoint'),
    url(r"^(?P<url>.*)/$", EndpointActivityViewSet.as_view(), name="endpoint-activity"),
]

urlpatterns += router.urls