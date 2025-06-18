from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
import torch
import os

from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
import os

HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
if HF_TOKEN:
    login(HF_TOKEN)  # Login using the token

model_path = "adityamukherjeeofficial/codegen-350M-mono"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

def get_code_hint(problem_description: str, user_code: str, test_input: str, expected_output: str, actual_output: str):
    prompt = f"""
You are an expert programming tutor. Your job is to look at the student's code and explain clearly what might be going wrong.

Problem description:
{problem_description}

Student's code:
{user_code}

Test case it failed:
Input: {test_input}
Expected Output: {expected_output}
Actual Output: {actual_output}

Give a detailed explaination to what is the error and why it is failing. Give a short paragraph, explaining, what was the bug in the code for not getting the correct output
Hint:"""

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=64,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

    full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    generated = full_output[len(prompt):].strip()

    # Return only the first non-empty line as hint
    hint = generated.split('\n')[0].strip()
    return hint
