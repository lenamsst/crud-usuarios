from fastapi import FastAPI
from .database import Base, engine
from .routers import users, login

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(login.router)
