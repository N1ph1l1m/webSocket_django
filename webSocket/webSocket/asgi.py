"""
ASGI config for webSocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import django
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from web_channels.routing import websocket_urlpatterns

# from web_channels.routing import websocket_urlpatterns

#from chat.middleware import JwtAuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webSocket.settings')

django_asgi_app = get_asgi_application()


#restchannels
#from chat import routing




#application = get_asgi_application()

# application = ProtocolTypeRouter({
#     'http' : get_asgi_application(),
#     "websocket" : JwtAuthMiddlewareStack(
#         URLRouter(
#             routing.websocket_urlpatterns
#         )
#     ),
# })



##channels

application = ProtocolTypeRouter(
    {
    "http":django_asgi_app,
    "websocket":AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    }
)