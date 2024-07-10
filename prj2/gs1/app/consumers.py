

from channels.consumer import SyncConsumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('connect...')
        self.send({
            'type':"websocket.accept"
        })
    def websocket_receive(self,event):
        print('message__receive....')
    def websocket_disconnect(self,event):
        print('disconnect....')