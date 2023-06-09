from fastapi import FastAPI
from .routers import post, user, auth
from . import models 
from .database import engine

# this ensures the sql alchemy models are implemented and created on the database

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# add more routers here when you add more functionality

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def get_home():
    return {'message': 'This is the home page.'}