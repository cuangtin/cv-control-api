from typing import Optional, List
from pydantic import BaseModel, Field
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

class CVModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    content: str = Field(...)
    link: str = Field(...)


class CVCollection(BaseModel):
    cv_list: List[CVModel]
