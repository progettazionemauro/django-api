from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Nation
from .serializers import NationSerializer

class NationAPIView(generics.ListCreateAPIView):
    queryset = Nation.objects.all()
    serializer_class = NationSerializer