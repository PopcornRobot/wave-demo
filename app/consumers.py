import json
from channels.generic.websocket import AsyncWebsocketConsumer # The class we're using
from asgiref.sync import sync_to_async # Implement later

class AdminConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("--- AdminConsumer -- connect")
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user = self.scope['url_route']['kwargs']['user']
        self.room_group_name = 'room_%s' % self.room_name

        print(self.user, self.room_name)

        if self.user != 'admin':
            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
                )
            print("channel layer group", self.room_group_name, self.channel_name)

        await self.accept()

    # Receive message from WebSocket
    async def receive(self, text_data):
        print("--- AdminConsumer -- receive")
        data = json.loads(text_data)
        action = data['action']
        message = data['message']
        username = data['username']
        room = data['room']
        print(action, message, username, room)
        room_group = 'room_%s' % room
        # Send message to room group
        await self.channel_layer.group_send(
            # self.room_group_name,
            # "game_test2",
            room_group,
            {
            'type': 'message',
            'message': 'message',
            'username': 'username',
            'action': action
            }
        )

    # Receive message from room group
    async def message(self, event):
        message = event['message']
        username = event['username']
        action = event['action']

        print('--- AdminConsumer -- message', message, username)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'action': action,
        }))

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("---- ChatConsumer -- connect" )
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
            )

        await self.accept()
        
    # Receive message from WebSocket
    async def receive(self, text_data):
        print("--- ChatConsumer -- receive")
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
            'type': 'chat_message',
            'message': message,
            'username': username
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
        self.room_group_name,
        self.channel_name
    )

 