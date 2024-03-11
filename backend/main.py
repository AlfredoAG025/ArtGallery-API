from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.base import Base
from db.session import engine
from core.config import settings

from apis.base import api_router

origins = [
    "*",
    # "http://localhost:4200",
    # "http://192.168.100.142:4200",
]


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"msg": "Hello FastAPI 🚀"}
