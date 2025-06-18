from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
import tempfile
import os
import subprocess
import uuid
from app.db.session import get_db
from app.crud import get_problem_by_id
from app.models.problem import Problem
from app.utils.hf_model import get_code_hint  # Adjust path if different


router = APIRouter()

class Submission(BaseModel):
    problem_id: int
    code: str
    language: str = "cpp"

@router.post("/submit")
async def submit_code(sub: Submission, db: AsyncSession = Depends(get_db)):
    problem = await get_problem_by_id(db, sub.problem_id)

    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found.")

    test_cases = problem.examples or []
    if not test_cases:
        raise HTTPException(status_code=404, detail="No test cases found for this problem.")

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            code_file = os.path.join(tmpdir, "submission.cpp")
            with open(code_file, "w") as f:
                f.write(sub.code)

            exec_file = os.path.join(tmpdir, "exec")
            compile_cmd = ["g++", code_file, "-o", exec_file]
            compile_result = subprocess.run(compile_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if compile_result.returncode != 0:
                return {
                    "status": "Compilation Error",
                    "message": compile_result.stderr.decode(),
                    "results": [],
                    "hint": None
                }
            results = []
            all_passed = True
            hint = None

            for i, case in enumerate(test_cases):
                try:
                    run_result = subprocess.run(
                        [exec_file],
                        input=case["input"].encode(),
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        timeout=2
                    )

                    user_output = run_result.stdout.decode().strip()
                    expected_output = case["output"].strip()
                    passed = user_output == expected_output

                    if not passed and hint is None:
                        # 🔥 Call model on the first failed case
                        hint = get_code_hint(
                            problem_description=problem.description,
                            user_code=sub.code,
                            test_input=case["input"],
                            expected_output=expected_output,
                            actual_output=user_output
                        )

                    if not passed or run_result.returncode != 0:
                        all_passed = False

                    result_obj = {
                        "test_case": i + 1,
                        "passed": passed,
                        "expected": expected_output,
                        "got": user_output
                    }

                    if run_result.returncode != 0:
                        result_obj["error"] = run_result.stderr.decode().strip()

                    results.append(result_obj)

                except subprocess.TimeoutExpired:
                    all_passed = False
                    results.append({
                        "test_case": i + 1,
                        "passed": False,
                        "error": "Time Limit Exceeded"
                    })

            return {
                "status": "Accepted" if all_passed else "Wrong Answer",
                "results": results,
                "message": None,
                "hint": None if all_passed else hint
            }

    except Exception as e:
        return {
            "status": "Error",
            "message": f"Internal server error: {str(e)}",
            "results": [],
            "hint": None
        }