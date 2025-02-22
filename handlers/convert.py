import requests
import config

def convert_code(source_code, from_lang, to_lang):
    """
    Converts code from one language to another using GPT-4o.
    """
    prompt = f"Convert the following {from_lang} code to {to_lang}:\n\n{source_code}"

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
