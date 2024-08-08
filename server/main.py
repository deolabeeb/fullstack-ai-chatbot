from fastapi import FastAPI, Request
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

api = FastAPI()

@api.get("/test")
async def root():
    return {"msg": "Adeola's API is Online"}

if __name__ == "__main__":
    if os.environ.get('APP_ENV') == "development":
        uvicorn.run("main:api", host="localhost", port=3500,
                    workers=4, reload=True)
    else:
        pass