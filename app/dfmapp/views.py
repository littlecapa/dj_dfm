from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Config
from .serializers import ConfigSerializer

class ConfigAPIView(APIView):
    def get(self, request):
        config = Config.objects.first()
        if config:
            serializer = ConfigSerializer(config)
            return Response(serializer.data)
        return Response({"error": "No configuration found"}, status=404)
