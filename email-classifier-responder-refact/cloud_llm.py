class CloudLLM:
    def __init__(self, model_name, api_key, api_base):
        self.model_name = model_name
        self.api_key = api_key
        self.api_base = api_base
        self.callbacks = []  # Initialize callbacks as an empty list

    def bind(self, *args, **kwargs):
        # Implement the bind method if required by the Agent class
        return self  # Return self or appropriate binding object

    # Add other methods as needed to interface with the cloud model
    def run(self, prompt):
        # Implement the method to run a prompt with the cloud model
        # This is a placeholder; you'll need to implement the actual API call
        return f"Running {prompt} with {self.model_name} on {self.api_base}"

    def __or__(self, other):
        # Ensure the class supports the 'or' operation if required by the Agent class
        return self
