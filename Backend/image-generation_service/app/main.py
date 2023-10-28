from fastapi import FastAPI
from routers import image_generation

app = FastAPI()

app.include_router(image_generation.generation)