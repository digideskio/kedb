
from rest_framework import serializers

from kedb.models import KnownError, Workaround

class WorkaroundSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Workaround
        fields = ('id', 'known_error', 'description', 'temporary', 'engine', 'action')

class KnownErrorSerializer(serializers.HyperlinkedModelSerializer):

    workarounds = WorkaroundSerializer(many=True)

    class Meta:
        model = KnownError
        fields = ('id', 'name', 'description', 'check', 'output_pattern', 'level', 'severity', 'ownership', 'workarounds')
