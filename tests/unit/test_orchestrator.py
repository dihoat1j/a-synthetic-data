from a_synthetic_data.agents import Agent
from a_synthetic_data.orchestrator import Orchestrator

def test_orchestrator_run() -> None:
    orch = Orchestrator()
    orch.register(Agent(name="planner", skills=["plan"]))
    out = orch.run("ship release")
    assert len(out.steps) == 3
