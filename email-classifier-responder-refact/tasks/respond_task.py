from crewai import Task

def create_respond_task(email, responder):
    return Task(
        description=f"Respond to the email: '{email}' based on the importance provided by the 'classifier' agent.",
        agent=responder,
        expected_output="A very concise response to the email based on the importance provided by the 'classifier' agent."
    )
