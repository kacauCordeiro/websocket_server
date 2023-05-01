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


# def on_message(ws, message):
#     print(message)

# def on_error(ws, error):
#     print(error)

# def on_close(ws, close_status_code, close_msg):
#     print("### closed ###")

# def on_open(ws):
#     print("Opened connection")

# async def start_server():
#     # async with websockets.serve(echo, "127.0.0.1", 8000):
#     #     print("Server started")
#     #     await asyncio.Future()  # run forever

#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("ws:localhost:8000",
#                               on_open=on_open,
#                               on_message=on_message,
#                               on_error=on_error,
#                               on_close=on_close)

#     ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
#     rel.signal(2, rel.abort)  # Keyboard Interrupt
#     rel.dispatch()
