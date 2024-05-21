import os
from langchain_community.llms import Ollama

def load_env_variables():
    model_name = os.getenv("OPENAI_MODEL_NAME")
    api_key = os.getenv("OPENAI_API_KEY")
    api_base = os.getenv("OPENAI_API_BASE")

    if not model_name or not api_key or not api_base:
        raise EnvironmentError("Please set the environment variables: OPENAI_MODEL_NAME, OPENAI_API_KEY, and OPENAI_API_BASE")
    
    return model_name, api_key, api_base

def get_llm_model():
    model_type = os.getenv("MODEL_TYPE", "groq")  # Default to groq if not set
    if model_type == "local":
        local_model_name = os.getenv("LOCAL_MODEL_NAME", "llama3:8b")
        print(f"Using local Llama3 model: {local_model_name}")
        return Ollama(model=local_model_name)
    else:
        model_name, api_key, api_base = load_env_variables()
        print(f"Using remote model: {model_name} with API base: {api_base}")
        # Set environment variables for the cloud model
        os.environ["OPENAI_API_BASE"] = api_base
        os.environ["OPENAI_MODEL_NAME"] = model_name
        os.environ["OPENAI_API_KEY"] = api_key
        return None  # For cloud model, no need to return an LLM instance

