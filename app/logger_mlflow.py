import mlflow
import os, time

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000"))
mlflow.set_experiment("simple-llmops-chatbot")

def log_interaction(model_name, prompt, response):
    with mlflow.start_run(run_name=model_name):
        mlflow.log_param("model", model_name)
        mlflow.log_param("timestamp", time.strftime("%Y-%m-%d %H:%M:%S"))
        mlflow.log_text(prompt, "prompt.txt")
        mlflow.log_text(response, "response.txt")
