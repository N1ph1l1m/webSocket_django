from os import path

from djangochannelsrestframework import consumers

webSocket_urlpatterns = [
    path("ws/",consumers.UserConsumer.as_asgi()),
    path("ws/chat/",consumers.RoomConsumer.as_asgi())
]