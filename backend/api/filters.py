import django_filters

from rates.models import Rate


class RateFilter(django_filters.FilterSet):
    """
    Фильтр для запросов к объектам модели Rate.

    Фильтрация осуществляется по char_code, date.
    """

    charcode = django_filters.CharFilter(
        field_name='char_code')

    class Meta:
        model = Rate
        fields = ('name', 'date')

    def filter_queryset(self, queryset):

        return super().filter_queryset(queryset)[:1]
