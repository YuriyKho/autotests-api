import asyncio

import websockets
from websockets import ServerConnection


# Обработчик входящих сообщений
async def echo(websocket: ServerConnection):
    message = await websocket.recv()
    print(f"Получено сообщение от пользователя: {message}")

    # Отправляем пять ответных сообщений
    for i in range(1, 6):
        response = f"{i} Сообщение пользователя: {message}"
        await websocket.send(response)
        # print(f"Отправлено сообщение {i}: {response}")

    # async for message in websocket:
    #     print(f"Получено сообщение от пользователя: {message}")
    #     response = f"Сервер получил: {message}"
    #     await websocket.send(response)  # Отправляем ответ


# Запуск WebSocket-сервера на порту 8765
async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())