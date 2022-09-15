from django.urls import path

from . import consumers

websocket_urlpatterns = [
  path('ws/admin/<str:user>/<str:room_name>', consumers.AdminConsumer.as_asgi()), # Using asgi
  path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()), # Using asgi
]