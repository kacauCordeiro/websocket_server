import asyncio
import logging
from websockets.server import serve

logging.basicConfig(level=logging.INFO)

async def echo(websocket, path):
    async for message in websocket:
        logging.info(f"Received message: {message}")
        await websocket.send(f"Received: {message}")

async def start_server():
    async with serve(echo, "0.0.0.0", 8000):
        print("Server started")
        logging.info(f"Message received {echo}")
        await asyncio.Future()  # run forever

asyncio.run(start_server())
