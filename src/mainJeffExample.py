import requests
import asyncio
from aiohttp import ClientSession

API_URL = "http://localhost:8051"

async def get_url(session):
    response = await session.get(API_URL)

async def get_stuff():
    async with ClientSession() as session:
        await asyncio.gather(*[get_url(session) for _ in range(10000)])

if __name__ == "__main__":
    asyncio.run(get_stuff())
