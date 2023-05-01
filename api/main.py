from fastapi import Body, FastAPI, WebSocket
from fastapi.responses import JSONResponse
from websockets.client import connect
from fastapi.responses import HTMLResponse
from api.pydantic.send_message_pydantic_model import MessagePydantic


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8080/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


app = FastAPI()
@app.get("/")
async def _index():
    """Exibe Api."""
    return JSONResponse(content={"status": 200, "message": "api-websocket alive v1.0"})

@app.get("/ws")
async def get():
    return HTMLResponse(html)

@app.post("/send_message")
async def send_message(message: MessagePydantic):
    async with connect("ws://websocket_server-websocket-1:8000") as websocket:
        await websocket.send(f"{message}")
        print(f"Received: {message}")
        await websocket.recv()
    return f"{message.message}"

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")