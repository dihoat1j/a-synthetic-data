from dataclasses import dataclass

@dataclass
class Agent:
    name: str
    skills: list[str]

    def can_handle(self, task: str) -> bool:
        return any(skill in task.lower() for skill in self.skills)
