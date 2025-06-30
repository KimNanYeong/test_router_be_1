from pydantic import BaseModel
from typing import Optional, List,Tuple
from datetime import datetime 
from fastapi import UploadFile, File


class TestRouter(BaseModel):
    name : str
