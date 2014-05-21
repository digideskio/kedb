
from rest_framework import serializers

from kedb.models import KnownError, Workaround

class WorkaroundErrorDetailSerializer(serializers.HyperlinkedModelSerializer):
	"""nejde reference primo na sebe coz je skoda"""
    class Meta:
        model = KnownError
        fields = ('id', 'name', 'description', 'check', 'output_pattern', 'level', 'severity', 'ownership')

class WorkaroundSerializer(serializers.HyperlinkedModelSerializer):

    error_detail = WorkaroundErrorDetailSerializer(many=False)

    class Meta:
        model = Workaround
        fields = ('id', 'known_error', 'description', 'temporary', 'engine', 'action', 'error_detail')
        nested = True

class KnownErrorSerializer(serializers.HyperlinkedModelSerializer):

    workarounds = WorkaroundSerializer(many=True)

    class Meta:
        model = KnownError
        fields = ('id', 'name', 'description', 'check', 'output_pattern', 'level', 'severity', 'ownership', 'workarounds')
        nested = True
