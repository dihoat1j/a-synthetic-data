from .agents import Agent

def select_agent(agents: list[Agent], task: str) -> Agent | None:
    for agent in agents:
        if agent.can_handle(task):
            return agent
    return agents[0] if agents else None
