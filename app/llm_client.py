import requests
import json
import os

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

def generate_response(model_name: str, prompt: str) -> str:
    payload = {"model": model_name, "prompt": prompt}
    r = requests.post(f"{OLLAMA_HOST}/api/generate", json=payload, stream=True)
    text = ""
    for line in r.iter_lines():
        if line:
            data = json.loads(line)
            if "response" in data:
                text += data["response"]
    return text.strip()
