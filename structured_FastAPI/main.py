from fastapi import FastAPI
from .routers import blog, users, authentication

app = FastAPI()

app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(blog.router)