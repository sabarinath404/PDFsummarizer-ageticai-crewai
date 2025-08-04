from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from project_seven.tools.pdf_reader_tool import PDFReaderTool

@CrewBase
class ProjectSeven():
    """ProjectSeven crew for EV analysis"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def pdf_summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['pdf_summarizer'],  # type: ignore[index]
            tools=[PDFReaderTool()],
            verbose=True
        )

    @agent
    def ev_benefits_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['ev_benefits_analyst'],  # type: ignore[index]
            tools=[PDFReaderTool()],
            verbose=True
        )

    @agent
    def ev_limitations_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['ev_limitations_analyst'],  # type: ignore[index]
            tools=[PDFReaderTool()],
            verbose=True
        )

    @task
    def summarize_pdf_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_pdf'],  # type: ignore[index]
        )

    @task
    def analyze_benefits_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_benefits'],  # type: ignore[index]
        )

    @task
    def analyze_limitations_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_limitations'],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ProjectSeven crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
