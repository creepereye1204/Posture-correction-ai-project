from django.urls import re_path
from .consumers import VideoConsumer

websocket_urlpatterns = [
    re_path(r"video", VideoConsumer.as_asgi()),
]
