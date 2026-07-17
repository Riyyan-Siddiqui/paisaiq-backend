from fastapi import FastAPI

from app.modules.auth.auth_router import router as auth_router

app = FastAPI()

app.include_router(auth_router)

@app.get('/')
def helloworld():
    return 'Hello world'