from crewai import Task

def create_classify_task(email, classifier):
    return Task(
        description=f"Classify the following email: '{email}'",
        agent=classifier,
        expected_output="One of these three options: 'important', 'casual', or 'spam'"
    )

def create_respond_task(email, responder):
    return Task(
        description=f"Respond to the email: '{email}' based on the importance provided by the 'classifier' agent.",
        agent=responder,
        expected_output="A very concise response to the email based on the importance provided by the 'classifier' agent."
    )
