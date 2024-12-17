from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.scene_routes import router as scene_router


app = FastAPI()

app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/")
async def root():
    return {"Hello": "Akshi"}

app.include_router(scene_router)
