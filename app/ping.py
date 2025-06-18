import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = os.getenv("API_URL")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

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

payload = {
    "inputs": prompt,
    "parameters": {
        "max_new_tokens": 64,
        "temperature": 0.2
    }
}

response = requests.post(API_URL, headers=headers, json=payload)
print("Status:", response.status_code)
print("Response:", response.text)
