from .agents import Agent

def score_agent(agent: Agent, task: str) -> int:
    return sum(1 for skill in agent.skills if skill in task.lower())

def select_agent(agents: list[Agent], task: str) -> Agent | None:
    ranked = sorted(agents, key=lambda a: score_agent(a, task), reverse=True)
    return ranked[0] if ranked else None
