"""
Program Overview:
Description: Simple email classifier between 2 agents. Agent #1 will receive an email
and classify it. Based on this classification, Agent #1 will write a response.

Credit: David Ondrej 👍
"""

# Import necessary modules and classes
import os
from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process

# Set environment variables for the API base, model name, and API key
os.environ["OPENAI_API_BASE"] = "[INSERT-API-BASE-FROM-GROQ]"
os.environ["OPENAI_MODEL_NAME"] = '[INSERT-MODEL-ID-FROM-GROQ]'
os.environ["OPENAI_API_KEY"] = '[INSERT-API-KEY-FROM-GROQ]'

# Sample email to be classified and responded to
email = "Your rent is due in 3 days."

# Define the classifier agent
classifier = Agent(
    role='email classifier',
    goal="accurately classify emails based on their importance. Give every email one of these ratings: important, casual, or spam.",
    backstory="You are an AI assistant whose only job is to classify emails accurately and honestly. Do not be afraid to give emails bad ratings if they are not important. Your job is to help the user manage their inbox.",
    verbose=True,
    allow_delegation=False
)

# Define the responder agent
responder = Agent(
    role="email responder",
    goal="Based on the importance of the email, write a concise and simple response. If the email is rated 'important' write a formal response, if the email is rated 'casual' write a casual response, and if the email is rated 'spam' ignore the email. No matter what, be very concise.",
    backstory="You are an AI assistant whose only job is to write short responses to emails based on their importance. The importance will be provided to you by the 'classifier' agent.",
    verbose=True,
    allow_delegation=False
)

# Define the task for classifying the email
classify_email = Task(
    description=f"Classify the following email: '{email}'",
    agent=classifier,
    expected_output="One of these three options: 'important', 'casual', or 'spam'"
)

# Define the task for responding to the email based on the classification
respond_to_email = Task(
    description=f"Respond to the email: '{email}' based on the importance provided by the 'classifier' agent.",
    agent=responder,
    expected_output="A very concise response to the email based on the importance provided by the 'classifier' agent."
)

# Create a crew with the classifier and responder agents and the tasks they need to perform
crew = Crew(
    agents=[classifier, responder],
    tasks=[classify_email, respond_to_email],
    verbose=2,
    process=Process.sequential
)

# Execute the tasks sequentially and print the output
output = crew.kickoff()
print(output)
