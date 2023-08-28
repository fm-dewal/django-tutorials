import json

from channels.generic.websocket import WebsocketConsumer
# Conversion to aynch
## from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone

## class ChatConsumer(AsyncWebsocketConsumer):
class ChatConsumer(WebsocketConsumer):
    ## async def connect(self):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

        ## Join room group
        ## await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        ## await self.accept()

    ## async def disconnect(self, close_code):
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
        ## Leave room group
        ## await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    ## async def receive(self, text_data):
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        
        # self.send(text_data=json.dumps({"message": message}))
        # Send message to room group
        # Sends an event to a group.
        # Event has a special 'type' key corresponding to the name of the method 
        #               that should be invoked on consumers that receive the event.
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                "type": "chat_input", # or chat.input
                "message": message, 
                "year": timezone.now().year,
            }
        )

        ## Send message to room group
        ## await self.channel_layer.group_send(
        ##    self.room_group_name, {
        ##       "type": "chat_input", 
        ##       "message": message,
        ##       "year": timezone.now().year,
        ##    }
        ## )

    # Receive message from room group
    ## async def chat_input(self, event):
    def chat_input(self, event):
        print("invoked")
        message = event["message"]
        year = event["year"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            "message": message,
            "year": year,
        }))

        ## await self.send(text_data=json.dumps({
        ##       "message": message,
        ##       "year": year,
        ## }))