import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    return {"msg": "hello mikigo"}


if __name__ == '__main__':
    uvicorn.run(
        app="server:app",
        host=os.popen("hostname -I").read().split(" ")[0],
        port=5000,
        reload=True
    )
