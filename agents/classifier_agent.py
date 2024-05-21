from crewai import Agent

def create_classifier_agent(llm_config):
    if llm_config is None:
        # Cloud model configuration
        return Agent(
            role='email classifier',
            goal="accurately classify emails based on their importance. Give every email one of these ratings: important, casual, or spam.",
            backstory="You are an AI assistant whose only job is to classify emails accurately and honestly. Do not be afraid to give emails bad ratings if they are not important. Your job is to help the user manage their inbox.",
            verbose=True,
            allow_delegation=False
        )
    else:
        # Local model (Ollama)
        return Agent(
            role='email classifier',
            goal="accurately classify emails based on their importance. Give every email one of these ratings: important, casual, or spam.",
            backstory="You are an AI assistant whose only job is to classify emails accurately and honestly. Do not be afraid to give emails bad ratings if they are not important. Your job is to help the user manage their inbox.",
            verbose=True,
            allow_delegation=False,
            llm=llm_config
        )
