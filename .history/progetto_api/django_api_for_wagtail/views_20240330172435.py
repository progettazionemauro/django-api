from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Nation
from .serializers import NationSerializer  # Add this line to import the serializer

# http://127.0.0.1:8085/django_api_for_wagtail/nations
class NationAPIView(APIView):
    def get(self, request):
        nations = Nation.objects.all()
        serializer = NationSerializer(nations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
