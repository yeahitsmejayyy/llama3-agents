import os

def load_env_variables():
    api_base = os.getenv("OPENAI_API_BASE")
    model_name = os.getenv("OPENAI_MODEL_NAME")
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_base or not model_name or not api_key:
        raise EnvironmentError("Please set the environment variables: OPENAI_API_BASE, OPENAI_MODEL_NAME, OPENAI_API_KEY")

    return api_base, model_name, api_key
