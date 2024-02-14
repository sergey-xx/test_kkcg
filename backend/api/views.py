from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



from rates.models import Rate
from .serializers import RateSerializer
from .filters import RateFilter


class PostViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    http_method_names = ['get',]
    permission_classes = [AllowAny, ]
    pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RateFilter
    filterset_fields = ('name',)
    filterset_fields = ('char_code', 'date')

    def list(self, request):
        currency_list = self.filter_queryset(self.queryset).values()
        return Response(currency_list)
