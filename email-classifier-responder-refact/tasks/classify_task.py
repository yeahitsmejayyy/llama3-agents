from crewai import Task

def create_classify_task(email, classifier):
    return Task(
        description=f"Classify the following email: '{email}'",
        agent=classifier,
        expected_output="One of these three options: 'important', 'casual', or 'spam'"
    )
