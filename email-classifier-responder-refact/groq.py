# Import necessary modules and classes
from dotenv import load_dotenv
from crewai import Crew, Process
from config import get_llm_model
from agents import create_classifier_agent, create_responder_agent
from tasks import create_classify_task, create_respond_task
 

# Load environment variables from .env file
load_dotenv()

# Get the LLM model based on environment configuration
llm_config  = get_llm_model()

# Initialize the LLM model for the cloud configuration if needed
# if not llm_model:
#     model_name = os.getenv("OPENAI_MODEL_NAME")
#     llm_model = Ollama(model=model_name)

# Print the LLM model configuration to debug
print(f"LLM Config: {llm_config }")

# Sample email to be classified and responded to
email = "Your rent is due in 3 days."

# Create agents
classifier = create_classifier_agent(llm_config)
responder = create_responder_agent(llm_config)

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
