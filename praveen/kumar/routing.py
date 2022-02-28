from django.urls import re_path

from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/kumar/(?P<room_name>\w+)/$', consumer.ChatConsumer.as_asgi()),
]