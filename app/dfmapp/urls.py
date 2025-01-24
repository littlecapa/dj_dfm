from django.urls import path
from .views import ConfigAPIView, LichessConfigAPIView

urlpatterns = [
    path('config/', ConfigAPIView.as_view(), name='config'),
    path('liconfig/', LichessConfigAPIView.as_view(), name='liconfig'),
]
