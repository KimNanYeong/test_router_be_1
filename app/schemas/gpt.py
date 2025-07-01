from pydantic import BaseModel
from fastapi import UploadFile, File


class gptAnswer(BaseModel):
    prompt: str