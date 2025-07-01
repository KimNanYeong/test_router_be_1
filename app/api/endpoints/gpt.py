from fastapi import APIRouter, HTTPException
import logging
from app.schemas.gpt import gptAnswer
from app.service.gpt import generate_content

router = APIRouter()

@router.post("/")
def get_gpt_answer(request: gptAnswer):
    try:
        answer = generate_content(request.prompt)
        return {
            "request": request.prompt,
            "response": answer
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="GPT 호출 중 오류 발생")