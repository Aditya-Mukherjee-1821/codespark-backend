from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.hf_model import get_code_hint

router = APIRouter()

class HintRequest(BaseModel):
    problem_description: str
    user_code: str
    test_input: str
    expected_output: str
    actual_output: str

@router.post("/get-hint/")
async def get_hint(payload: HintRequest):
    hint = get_code_hint(
        problem_description=payload.problem_description,
        user_code=payload.user_code,
        test_input=payload.test_input,
        expected_output=payload.expected_output,
        actual_output=payload.actual_output
    )
    return {"hint": hint}
