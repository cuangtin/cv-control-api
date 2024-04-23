from fastapi import APIRouter, Request, HTTPException, status
from typing import List, Union
from bson import ObjectId

from models import CV

router = APIRouter()

search_result = []

@router.get("/search", response_description="List all CVs", response_model=List[CV])
def list_cv(request: Request, q: Union[str, None] = None):
    # search_result = list[model]
    return list(request.app.database["list"].find(limit=100))


@router.get("/get/{id}", response_description="Get a single CV by id", response_model=CV)
def show_cv(id: str, request: Request):
    # filter from search_result()
    if (cv := request.app.database["list"].find_one({"_id": id})) is not None:
        return cv

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"ID {id} not found")
