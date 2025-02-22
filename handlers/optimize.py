import requests
import config

def optimize_code(code_snippet):
    """
    Optimizes a given code snippet using GPT-4o.
    """
    prompt = f"Optimize the following code for better efficiency and readability:\n\n{code_snippet}"

    headers = {
        "Authorization": f"Bearer {config.API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"
