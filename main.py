from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.scene_routes import router as scene_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"Hello": "Akshi"}

app.include_router(scene_router)
