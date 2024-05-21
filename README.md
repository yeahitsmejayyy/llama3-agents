# Llama3 Agents
![Folder Structure](llama3_agents_cover.png)




## Backstory
I was inspired to create this project after watching a YouTube video on using Llama3 models for AI tasks. The tutorial provided a basic working example, and I decided to refactor the code to make it more modular. Additionally, I implemented a configuration layer to easily switch between local and cloud setups.

## Project Overview

This repository serves as a boilerplate for quickly getting started with both local and cloud setups when working with large language models (LLMs). The primary goal is to provide a modular and easily configurable example of using agents to perform tasks that solve real-world problems. 

### Purpose
The project demonstrates how two agents can be used to solve the problem of auto-labeling and responding to emails. By using a classifier agent and a responder agent, the program can determine the importance of an email and generate an appropriate response based on the classification.

### Capabilities
- **Email Classification:** The classifier agent evaluates the content of an email and labels it as either 'important,' 'casual,' or 'spam.'
- **Email Response:** Based on the classification, the responder agent generates a concise and relevant response to the email.

### Extensibility
This project is a foundational example and can be extended to create various types of Agent Swarms. These swarms can handle more complex workflows, integrate with different types of data sources, or perform additional tasks. The modular design allows developers to build on top of this example and enhance it to meet specific needs.


Feel free to explore, modify, and expand the capabilities of this project to suit your specific use case.


## Folder Structure

```
.
├── agents
│ ├── classifier_agent.py
│ └── responder_agent.py
├── tasks
│ ├── classify_task.py
│ └── respond_task.py
├── .env
├── config.py
├── groq.py
├── local.py
└── README.md
```

---

### Agents 😎
- `classifier_agent.py`: Defines the classifier agent.
- `responder_agent.py`: Defines the responder agent.

---

### Tasks ✔
- `classify_task.py`: Defines the classification task.
- `respond_task.py`: Defines the response task.

---

### Configuration Files ⚙
- `.env`: Environment variables for model configuration.
- `config.py`: Configuration logic for selecting the model.

---

### Execution Scripts
- `groq.py`: Runs the project using the cloud-based Llama3 model.
- `local.py`: Runs the project using the local Llama3 model.

---

## Setup Instructions

### Prerequisites
1. **Ollama**: Download the model installer called {:target="_blank"}. It is recommended to use the llama3:8b model, as the llama3:70b model requires a powerful computer. After installing the Ollama app, download the model by [clicking here](https://ollama.com/library/llama3){:target="_blank"} and running the command shown on the screen in your terminal.
   
2. **Python**: Ensure Python is installed on your computer. You can download it from [here](https://www.python.org/downloads/){:target="_blank"}.

3. **Groq**: Set up an account with [Groq](https://console.groq.com/login). Create your API keys [here](https://console.groq.com/keys) and get the base_url from [here](https://console.groq.com/docs/openai).

4. **Environment Variables**: Update your `.env` file with the appropriate environment variables.



### Steps

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install dependencies**:
    ```sh
    pip install os langchain_community.llms dotenv crewai
    ```

3. **Setup your .env file** with the appropriate keys:
    ```env
    OPENAI_API_BASE=<your-api-base-url>
    OPENAI_MODEL_NAME=<your-model-name>
    OPENAI_API_KEY=<your-api-key>
    LOCAL_MODEL_NAME=llama3:8b
    MODEL_TYPE=local  # Change to `groq` for cloud model
    ```

4. **Run the program**:
    - For the local model:
      ```sh
      python local.py
      ```

    - For the cloud model:
      ```sh
      python groq.py
      ```



**Important Note**: Ensure you set the environment in your `.env` file to either "local" for the local model setup or "groq" for the cloud model setup.




### Credits 🍻
I would like to give credit to the original creator whose video I watched named [David Ondrej](https://www.youtube.com/@DavidOndrej), who inspired me to create this projects initial setup and structure for his email responder example.

### License
This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for details.