import asyncio
import random
import time
from websockets.client import connect


lista_json = [
    {
        "timestamp": "2023-05-22T10:30:00",
        "sensor_id": "A123",
        "location": "Sala 1",
        "temperature": 25.5,
        "humidity": 45.2,
        "unit": {
            "temperature": "Celsius",
            "humidity": "Percent"
        }
    },
    {
        "timestamp": "2023-05-22T10:35:00",
        "sensor_id": "A456",
        "location": "Sala 2",
        "temperature": 24.8,
        "humidity": 42.1,
        "unit": {
            "temperature": "Celsius",
            "humidity": "Percent"
        }
    },
    {
        "timestamp": "2023-05-22T10:40:00",
        "sensor_id": "A789",
        "location": "Sala 3",
        "temperature": 26.2,
        "humidity": 48.6,
        "unit": {
            "temperature": "Celsius",
            "humidity": "Percent"
        }
    },
    # Adicione mais objetos JSON aqui
    {
        "timestamp": "2023-05-22T11:25:00",
        "sensor_id": "B123",
        "location": "Sala 4",
        "temperature": 27.9,
        "humidity": 41.8,
        "unit": {
            "temperature": "Celsius",
            "humidity": "Percent"
        }
    }
]

async def send_message():
    
    async with connect("ws://websocket:8080/ws") as websocket:
        while True:
            message = random.choice(lista_json)
            await websocket.send(f"{message}")
            print(f"Received: {message}")
            await websocket.recv()
            websocket.close()
            await asyncio.sleep(10)

loop = asyncio.get_event_loop()
loop.run_until_complete(send_message())