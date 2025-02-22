from openai import OpenAI
import config

def explain_code(code: str):
    client = OpenAI(api_key=config.GPT4O_API_KEY)

    response = client.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Explain this code:\n{code}"}],
    )

    return response.choices[0].message["content"]
