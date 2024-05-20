# Llama3 Agents

## Program Overview

This project implements a simple email classifier and responder using two agents. The first agent, Agent #1, classifies the importance of incoming emails. Based on this classification, Agent #2 generates an appropriate response. This system leverages the `Ollama` language model and the `crewai` library to achieve its functionality.

## Features

- **Email Classification**: Classifies emails into one of three categories: `important`, `casual`, or `spam`.
- **Automated Responses**: Generates concise responses based on the email classification.
- **Sequential Task Processing**: Processes tasks sequentially using a crew of agents.

## Requirements

- Python 3.7 or higher
- `langchain_community` library
- `crewai` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/email-classifier-responder.git
    cd email-classifier-responder
    ```

2. Install the required libraries:

    ```sh
    pip install langchain_community crewai
    ```

## Environment Variables

Before running the program, set the following environment variables with your respective values:

- `OPENAI_API_BASE`: The base URL for the OpenAI API.
- `OPENAI_MODEL_NAME`: The model ID to be used.
- `OPENAI_API_KEY`: Your OpenAI API key.

You can set these variables in your terminal or in a `.env` file.

## Usage

There are two main ways to run this program:

1. **Using `groq.py`**:
   - This approach taps into llama3 models online using Groq's infrastructure.
   - Recommended for most users to avoid the need for powerful local hardware.
   
    ```sh
    python groq.py
    ```

2. **Using `main.py`**:
   - This approach allows you to run the program using your local version of the llama3 model.
   - Only recommended if you have a very powerful computer capable of handling the model locally.

    ```sh
    python main.py
    ```

### Disclaimer

Unless you have a really powerful computer, it is recommended to use `groq.py` as you can leverage the power of Groq's infrastructure and computers, avoiding potential crashes and performance issues on your own machine.

### Downloading a Local Version of Llama3

To run the llama3 model locally, follow these steps:

1. Go to [https://ollama.com](https://ollama.com) to download the installer.
2. On the home page, go to 'Models' and select 'llama3'.
3. Choose the version you want to download, either '8B' or '70B'. **Note:** Unless you have a very powerful machine, it is not recommended to run the '70B' model locally.
4. Once downloaded, you can run the model locally using the command:
    ```sh
    ollama run llama:8b
    ```
    This will allow you to interact with the model via the command line or use this model with your local program as illustrated in `main.py`.

### Code Explanation

The code initializes two agents:
- **Classifier Agent**: Classifies emails based on their importance.
- **Responder Agent**: Generates responses based on the classification provided by the Classifier Agent.

Here is a brief description of the main components:

- **Agent Initialization**: Defines the roles, goals, backstories, verbosity, and delegation properties for both agents.
- **Task Definition**: Defines tasks for classifying and responding to emails.
- **Crew Initialization**: Groups the agents and tasks into a crew and sets the processing mode to sequential.
- **Execution**: Executes the tasks sequentially and prints the output.

### Sample Email

The sample email used in the program is:

```plaintext
Your rent is due in 3 days.
```

### Output
The program classifies the email and generates an appropriate response, which is then printed to the console.

### Credits
I would like to give credit to the original creator whose video I watched named [David Ondrej](https://www.youtube.com/@DavidOndrej), who provided this initial setup and structure for this email responder example.

### License
This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for details.