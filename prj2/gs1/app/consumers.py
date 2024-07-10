from time import sleep
import asyncio
from channels.consumer import SyncConsumer,AsyncConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('connect...')
        self.send({
            'type':"websocket.accept"
        })
    def websocket_receive(self,event):
        print('message__receive....')
        print(event['text'])
        self.send({
            'type':'websocket.send',
            'text':'this is the message from server'
            
        })
        for i in range(50):
            self.send({
                    'type':'websocket.send',
                    'text':f"{i}"  
                    })
            sleep(1)
             
            
             
    def websocket_disconnect(self,event):
        print('disconnect....')
        
        
        
        
        
        
class MyAsyncConsumer(AsyncConsumer):
   async def websocket_connect(self,event):
        print('connect...')
        await self.send({
            'type':"websocket.accept"
        })
        
   async def websocket_receive(self,event):
        print('message__receive....')
        print(event['text'])
        await self.send({
            'type':'websocket.send',
            'text':'this is the message from server'
            
        })
        for i in range(50):
            await self.send({
                    'type':'websocket.send',
                    'text':f"{i}"  
                    })
            await  asyncio.sleep(1)
             
            
             
   async def websocket_disconnect(self,event):
        print('disconnect....')