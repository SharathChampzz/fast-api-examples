# database.py
from typing import List
from pydantic import BaseModel

# Simulated in-memory database
class Item(BaseModel):
    id: int
    name: str
    description: str

# A dummy database as a list
db: List[Item] = []
