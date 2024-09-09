import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


## синхронный код
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        print( 'connect - scope = > ' + self.room_name)

        # Получает 'room_name'параметр из маршрута URL, chat/routing.py открывшего соединение WebSocket с потребителем.
        # У каждого потребителя есть область действия , содержащая информацию о его подключении, включая, в частности, любые позиционные или ключевые аргументы из маршрута URL,
        # а также информацию о текущем аутентифицированном пользователе, если таковой имеется.

        self.room_group_name = f"chat_{self.room_name}"

        #Создает имя группы каналов непосредственно из указанного пользователем имени комнаты, без кавычек или экранирования.
        # Имена групп могут содержать только буквы, цифры, дефисы, подчеркивания или точки. Поэтому этот пример кода не будет работать с именами комнат, которые содержат другие символы.


        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        #Присоединяется к группе.

        #Обертка async_to_sync(...)необходима, поскольку ChatConsumer является синхронным WebsocketConsumer, но он вызывает асинхронный метод уровня канала. (Все методы уровня канала являются асинхронными.)
        #Имена групп ограничены только буквами ASCII, цифрами, дефисами и точками и ограничены максимальной длиной 100 в бэкэнде по умолчанию.
        # Поскольку этот код создает имя группы непосредственно из имени комнаты, он завершится ошибкой, если имя комнаты содержит какие-либо символы, недопустимые в имени группы, или превышает ограничение по длине.

        self.accept()

        #Принимает соединение WebSocket.
        #Если вы не вызовете accept()внутри connect()метода, то соединение будет отклонено и закрыто.
        # Вы можете захотеть отклонить соединение, например, потому что запрашивающий пользователь не авторизован для выполнения запрошенного действия.
        #Рекомендуется accept()вызывать это действие в качестве последнегоconnect() , если вы решите принять соединение.


    def disconnect(self,close_code):
        #Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
        #Покидает группу.

        #receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]


        #Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type":"chat.message", "message":message }
        )
        #Отправляет событие в группу.
        #Событие имеет специальный 'type'ключ, соответствующий имени метода, который должен быть вызван для потребителей, получающих событие.
        # Этот перевод выполняется путем замены .на _, таким образом, в этом примере chat.message вызывается chat_message метод.


    def chat_message(self, event):
        message = event["message"]

        # send message to websocket
        self.send(text_data=json.dumps({"message":message}))

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = f"chat_{self.room_name}"
#
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)
#
#         await self.accept()
#
#
#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
#
#
#
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#
#         await self.channel_layer.group_send(
#             self.room_group_name, {"type":"chat.message","message":message}
#         )
#
#     async def chat_message(self, event):
#         message = event["message"]
#
#         await self.send(text_data=json.dumps({"message":message}))

