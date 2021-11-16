from pydantic import BaseModel
from typing import List


class Task(BaseModel):
    user_id: str
    user_name: str
    name: str
    description: str
    start_date: str
    end_date: str

