from django.urls import path
from. import consumers



websocket_urlpatterns=[
    path('', consumers.MySyncConsumer.as_asgi()),
    
]