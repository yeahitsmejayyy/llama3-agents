# Import necessary modules and classes
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from config import load_env_variables
from agents import create_classifier_agent, create_responder_agent
from tasks import create_classify_task, create_respond_task

# Load environment variables from .env file
load_dotenv()

# Load environment variables and check if they are set
api_base, model_name, api_key = load_env_variables()

# Check if the environment variables are set
if not api_base or not model_name or not api_key:
    raise EnvironmentError("Please set the environment variables: OPENAI_API_BASE, OPENAI_MODEL_NAME, OPENAI_API_KEY")

# Sample email to be classified and responded to
email = "Your rent is due in 3 days."

# Create agents
classifier = create_classifier_agent()
responder = create_responder_agent()

# Create tasks
classify_email = create_classify_task(email, classifier)
respond_to_email = create_respond_task(email, responder)

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
