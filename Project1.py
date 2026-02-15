import requests
import json

# Your GitHub Personal Access Token (PAT)
GITHUB_TOKEN = "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"
headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
# The endpoint for GitHub's chat completions
# This example uses Llama-3-70b-Instruct, which is excellent for your task
API_URL = "https://models.inference.ai.azure.com/chat/completions"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json"
}

system_instruction = """
You are an expert Lead Response Assistant.
1. Identify the core maintenance issue.
2. Ask 3 clarifying questions.
3. Provide safe next steps.
4. Maintain a professional and empathetic tone.
"""

def generate_reply(user_query):
    payload = {
        "messages": [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": user_query}
    ],
    # Try one of these IDs:
    "model": "gpt-4o-mini", 
    # Alternatives: "gpt-4o", "gpt-4o-mini", "Phi-3.5-mini-instruct"
    "temperature": 0.7,
    "max_tokens": 500
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

# User Input
user_input = input("Enter your Query: ")
print("\n--- AI Response ---\n")
print(generate_reply(user_input))