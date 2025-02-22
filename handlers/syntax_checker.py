import requests
import config

def check_syntax(code_snippet, language):
    """
    Checks and corrects syntax errors in the given code using GPT-4o.
    """
    prompt = f"Check and fix any syntax errors in the following {language} code:\n\n{code_snippet}"

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
