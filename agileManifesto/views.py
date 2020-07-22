from django.shortcuts import render
from rest_framework import viewsets
from agileManifesto.models import Principal, Value
from agileManifesto.serializers import ValueSerializer, PrincipalSerializer


# ---------Value View --------------#
class ValueViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer


# ---------Principal View --------------#
class PrincipalViewSet(viewsets.ModelViewSet):
    queryset = Principal.objects.all()
    serializer_class = PrincipalSerializer
