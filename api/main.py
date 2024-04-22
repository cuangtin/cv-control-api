from fastapi import APIRouter

from api.routes import cvs

api_router = APIRouter()
api_router.include_router(cvs.router, prefix="/cvs", tags=["items"])
