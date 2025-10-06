import json
from app.llm_client import generate_response

def run_eval(model="llama3", eval_file="data/eval_prompts.jsonl"):
    with open(eval_file) as f:
        for line in f:
            item = json.loads(line)
            prompt, expected = item["prompt"], item["expected"]
            output = generate_response(model, prompt)
            passed = expected.lower() in output.lower()
            print(f"Prompt: {prompt}\n→ Output: {output}\n✅ Pass: {passed}\n")

if __name__ == "__main__":
    run_eval()
