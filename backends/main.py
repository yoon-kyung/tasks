import uvicorn
from fastapi import FastAPI

from backends.apps.api import *
from backends.core import consts

from fastapi.middleware.cors import CORSMiddleware

from backends.database.sql.crud import patch_task

origins = ["http://localhost:8080", "https://localhost:8080"]


def include_router(app):
    app.include_router(get_api.ROUTER)
    app.include_router(post_api.ROUTER)
    app.include_router(patch_api.ROUTER)
    app.include_router(delete_api.ROUTER)


def start_application():
    app = FastAPI(title=consts.PROJECT_NAME, version=consts.PROJECT_VERSION)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    include_router(app)
    return app


app = start_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
