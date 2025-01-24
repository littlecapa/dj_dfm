from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Config, LichessConfigModel
from .serializers import ConfigSerializer, LichessConfigSerializer

class ConfigAPIView(APIView):
    def get(self, request):
        config = Config.objects.first()
        if config:
            serializer = ConfigSerializer(config)
            return Response(serializer.data)
        return Response({"error": "No configuration found"}, status=404)
    
class LichessConfigAPIView(APIView):
    def get(self, request):
        config = LichessConfigModel.objects.first()
        print(config)
        if config:
            serializer = LichessConfigSerializer(config)
            return Response(serializer.data)
        return Response({"error": "No Lichess configuration found"}, status=404)
