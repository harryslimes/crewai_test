import yaml
from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class EmailResponderCrew():
    agents_config  = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self, default_model=None) -> None:
        self.llm = Ollama(model=default_model, temperature = 0.0)

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = 2
        )
    @agent
    def email_classifier(self) -> Agent:
        return Agent(
            config = self.agents_config["email_classifier"],
            llm = self.llm
        )
    
    @agent
    def email_responder(self) -> Agent:
        return Agent(
            config = self.agents_config["email_responder"],
            llm = self.llm
        )

    @task
    def classify_email(self) -> Task:
        return Task(
            config = self.tasks_config['classify_email'],
            agent = self.email_classifier()
        )

    @task
    def generate_email(self) -> Task:
        return Task(
            config = self.tasks_config['generate_email_response'],
            agent = self.email_responder()
        )
    
    

    
