from crewai import Agent

def create_classifier_agent():
    return Agent(
        role='email classifier',
        goal="accurately classify emails based on their importance. Give every email one of these ratings: important, casual, or spam.",
        backstory="You are an AI assistant whose only job is to classify emails accurately and honestly. Do not be afraid to give emails bad ratings if they are not important. Your job is to help the user manage their inbox.",
        verbose=True,
        allow_delegation=False
    )

def create_responder_agent():
    return Agent(
        role="email responder",
        goal="Based on the importance of the email, write a concise and simple response. If the email is rated 'important' write a formal response, if the email is rated 'casual' write a casual response, and if the email is rated 'spam' ignore the email. No matter what, be very concise.",
        backstory="You are an AI assistant whose only job is to write short responses to emails based on their importance. The importance will be provided to you by the 'classifier' agent.",
        verbose=True,
        allow_delegation=False
    )
