
from rest_framework import serializers

from kedb.models import KnownError, Workaround

class KnownErrorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = KnownError
        fields = ('id', 'name', 'description', 'check', 'output_pattern', 'level', 'severity')


class WorkaroundSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Workaround
        fields = ('id', 'known_error', 'description', 'temporary')
