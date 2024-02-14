from rest_framework import serializers
from rates.models import Rate


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ('char_code',
                  'date',
                  'rate', )
        read_only_fields = ('char_code',
                            'date',
                            'rate', )
