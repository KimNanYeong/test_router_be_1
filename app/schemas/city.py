from pydantic import BaseModel
from fastapi import UploadFile, File

class Cityinfo(BaseModel):
    city_id: int
    city: str
