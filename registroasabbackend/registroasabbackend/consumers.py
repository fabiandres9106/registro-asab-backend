import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TicketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("tickets", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("tickets", self.channel_name)

    async def receive(self, text_data):
        await self.channel_layer.group_send("tickets", {
            "type": "ticket_message",
            "message": text_data
        })

    async def ticket_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            "message": message
        }))