from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "Salesforce/codegen-350M-mono"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

def get_hint_locally(prompt: str):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=64,
        temperature=0.7,
        do_sample=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    prompt = """
You're a helpful programming tutor.
A student submitted the following code for the problem:

"Find the maximum number in a list."

Code:
def max_elem(lst): return lst[0]

It fails on this test case:
Input: [3, 5, 2]
Expected Output: 5
Actual Output: 3

Give a short one-line hint about what might be wrong.
"""

    hint = get_hint_locally(prompt)
    print("\nHint:\n", hint)
