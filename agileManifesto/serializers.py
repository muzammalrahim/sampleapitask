from rest_framework import serializers
from agileManifesto.models import Value, Principal


# Value Serializer
class ValueSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Value
        fields = ("id", "value")


# Principal Serializer
class PrincipalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Principal
        fields = ("id", "principal")
