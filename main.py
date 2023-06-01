from fastapi import FastAPI
from .routers import post, user



# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
def get_home():
    return {'message': 'This is the home page.'}