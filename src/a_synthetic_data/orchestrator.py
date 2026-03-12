from .agents import Agent
from .delegation import select_agent
from .memory import SharedMemory
from .types import RunResult

class Orchestrator:
    def __init__(self) -> None:
        self.agents: list[Agent] = []
        self.memory = SharedMemory()

    def register(self, agent: Agent) -> None:
        self.agents.append(agent)

    def run(self, goal: str) -> RunResult:
        steps: list[str] = []
        for task in ["plan", "execute", "summarize"]:
            agent = select_agent(self.agents, task)
            owner = agent.name if agent else "unassigned"
            step = f"{task}:{owner}"
            steps.append(step)
            self.memory.put(task, owner)
        return RunResult(summary=f"Goal completed: {goal}", steps=steps)
