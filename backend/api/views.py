from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from rates.models import Rate
from .serializers import RateSerializer
from .filters import RateFilter


class PostViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    http_method_names = ['get', ]
    permission_classes = [AllowAny, ]
    pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RateFilter
    filterset_fields = ('name',)
    filterset_fields = ('char_code', 'date')
