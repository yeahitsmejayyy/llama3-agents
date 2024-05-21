from crewai import Agent

def create_responder_agent(llm_config):
    if llm_config is None:
        # Cloud model configuration
        return Agent(
            role="email responder",
            goal="Based on the importance of the email, write a concise and simple response. If the email is rated 'important' write a formal response, if the email is rated 'casual' write a casual response, and if the email is rated 'spam' ignore the email. No matter what, be very concise.",
            backstory="You are an AI assistant whose only job is to write short responses to emails based on their importance. The importance will be provided to you by the 'classifier' agent.",
            verbose=True,
            allow_delegation=False
        )
    else:
        # Local model (Ollama)
        return Agent(
            role="email responder",
            goal="Based on the importance of the email, write a concise and simple response. If the email is rated 'important' write a formal response, if the email is rated 'casual' write a casual response, and if the email is rated 'spam' ignore the email. No matter what, be very concise.",
            backstory="You are an AI assistant whose only job is to write short responses to emails based on their importance. The importance will be provided to you by the 'classifier' agent.",
            verbose=True,
            allow_delegation=False,
            llm=llm_config
        )
