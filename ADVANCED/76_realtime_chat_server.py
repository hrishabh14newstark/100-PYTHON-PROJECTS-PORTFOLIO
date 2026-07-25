"""
76: Real-Time Chat Server
Handle concurrent users with WebSockets and asyncio.
"""
import asyncio

async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    print(f"Received message: {message}")
    writer.close()

if __name__ == "__main__":
    print("Asyncio socket chat server ready.")
