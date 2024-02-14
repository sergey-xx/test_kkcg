from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from rates.models import Rate
from .serializers import RateSerializer

class RateViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    http_method_names = ['get', ]
    permission_classes = [AllowAny, ]
    pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)
    filterset_fields = ('charcode', 'date')

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data:
            response.data = response.data[0]
        return super().finalize_response(request, response, *args, **kwargs)
