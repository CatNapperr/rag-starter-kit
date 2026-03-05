from pydantic import BaseModel
from typing import List, Dict

class QARequest(BaseModel):
    question: str

class UrlRequest(BaseModel):
    url: str
