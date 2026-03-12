from dataclasses import dataclass

@dataclass
class RunResult:
    summary: str
    steps: list[str]
