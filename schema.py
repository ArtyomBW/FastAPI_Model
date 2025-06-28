from typing import Union
from pydantic import BaseModel


class CategoryForm(BaseModel):
    name: str

