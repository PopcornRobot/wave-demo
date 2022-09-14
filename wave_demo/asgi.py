import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
django.setup()

import app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wave_demo.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
    URLRouter(
      app.routing.websocket_urlpatterns
    )
  )
})
