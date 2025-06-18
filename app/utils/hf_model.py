from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

# Set the model repo path
model_path = "adityamukherjeeofficial/codegen-350M-mono"

# Optional: set token if model is private
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Load tokenizer and model from Hugging Face
tokenizer = AutoTokenizer.from_pretrained(model_path, use_auth_token=HF_TOKEN)
model = AutoModelForCausalLM.from_pretrained(model_path, use_auth_token=HF_TOKEN)

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
