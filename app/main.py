from fastapi import FastAPI, Request
from app.llm_client import generate_response
from app.logger_mlflow import log_interaction

app = FastAPI(title="Simple LLMOps Chatbot")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("prompt", "")
    model_name = data.get("model", "llama3")
    response = generate_response(model_name, user_input)

    # Log to MLflow
    log_interaction(model_name=model_name, prompt=user_input, response=response)

    return {"model": model_name, "response": response}
