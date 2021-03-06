from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/")
async def index():
    # await asyncio.sleep(1)
    return {"message": "hello world!"}
