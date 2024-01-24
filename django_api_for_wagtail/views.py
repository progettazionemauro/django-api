from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Nation
from .serializers import NationSerializer

class NationAPIView(generics.ListCreateAPIView):
    queryset = Nation.objects.all()
    serializer_class = NationSerializer
    
    def list(self, request, *args, **kwargs):
        nations = self.get_queryset()
        return render(request, 'nations_list.html', {'nations': nations})