from typing import Any, List, Union
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from models import (
    CVModel,
    CVCollection
)
router = APIRouter()


@router.get(
    "/",
    response_model=CVModel,
)
def list_cv(q: Union[str, None] = None, limit: int = 100) -> Any:
    cvs: List[CVModel]


@router.get("/{cv_id}", response_model=CVModel)
def show_cv(cv_id: str):
    """
    Get the record for a specific cv, looked up by `id`.
    """
    if (
        cv := student_collection.find_one({"_id": ObjectId(cv_id)})
    ) is not None:
        return cv

    raise HTTPException(status_code=404, detail=f"CV {id} not found")