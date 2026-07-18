from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.modules.auth.auth_router import router as auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins = [
        "*"
    ],

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

@app.get('/')
def helloworld():
    return 'Hello world'