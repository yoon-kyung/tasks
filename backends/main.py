from starlette.responses import JSONResponse
import uvicorn
from fastapi import FastAPI

from backends.apps.api import *
from backends.core import consts

from fastapi.middleware.cors import CORSMiddleware

from fastapi.exceptions import RequestValidationError


origins = ["http://localhost:8080", "https://localhost:8080"]

app = FastAPI(title=consts.PROJECT_NAME, 
                version=consts.PROJECT_VERSION)

# validation 통과하지 않는 경우 status code: 400
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=400, content=dict(msg=str(exc)))


def include_router(app):
    app.include_router(get_api.ROUTER)
    app.include_router(post_api.ROUTER)
    app.include_router(patch_api.ROUTER)
    app.include_router(delete_api.ROUTER)


def start_application():
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
