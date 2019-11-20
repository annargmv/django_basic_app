from django.shortcuts import render

from rest_framework import generics

from .models import Backend
from .serializers import BackendSerializer


class ListBackend(generics.ListCreateAPIView):
    queryset = Backend.objects.all()
    serializer_class = BackendSerializer


class DetailBackend(generics.RetrieveUpdateDestroyAPIView):
    queryset = Backend.objects.all()
    serializer_class = BackendSerializer
