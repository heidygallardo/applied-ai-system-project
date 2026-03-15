from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Data classes — simple value-holding objects (Task, Pet)
# ---------------------------------------------------------------------------

@dataclass
class Task:
    name: str
    duration: int          # minutes
    priority: str          # "low" | "medium" | "high"
    category: str
    frequency: str = "once"   # "once" | "daily" | "weekly" | "monthly"
    completed: bool = False

    def update_priority(self, new_priority: str) -> None:
        self.priority = new_priority

    def update_duration(self, new_duration: int) -> None:
        self.duration = new_duration

    def update_frequency(self, new_frequency: str) -> None:
        self.frequency = new_frequency

    def mark_complete(self) -> None:
        self.completed = True

    def get_task_info(self) -> dict:
        return {
            "name": self.name,
            "duration": self.duration,
            "priority": self.priority,
            "category": self.category,
            "frequency": self.frequency,
            "completed": self.completed,
        }


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def edit_task(self, task_name: str, **updates) -> None:
        for task in self.tasks:
            if task.name == task_name:
                for key, value in updates.items():
                    setattr(task, key, value)

    def remove_task(self, task_name: str) -> None:
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def get_tasks(self) -> list[Task]:
        return self.tasks


# ---------------------------------------------------------------------------
# Regular classes — objects with richer behavior (Owner, Scheduler)
# ---------------------------------------------------------------------------

class Owner:
    def __init__(self, name: str, availability: Optional[list] = None, preferences: Optional[dict] = None):
        self.name: str = name
        self.availability: list = availability or []
        self.preferences: dict = preferences or {}
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        pass

    def edit_pet(self, pet_name: str, **updates) -> None:
        pass

    def remove_pet(self, pet_name: str) -> None:
        pass

    def view_pets(self) -> list[Pet]:
        pass

    def view_all_tasks(self) -> list[Task]:
        pass


class Scheduler:
    def __init__(self, tasks: Optional[list[Task]] = None, availability: Optional[list] = None):
        self.tasks: list[Task] = tasks or []
        self.availability: list = availability or []
        self.daily_plan: list[Task] = []
        self.explanation: str = ""

    def generate_plan(self) -> None:
        pass

    def sort_tasks_by_priority(self) -> list[Task]:
        pass

    def filter_tasks_by_time(self) -> list[Task]:
        pass

    def build_explanation(self) -> str:
        pass

    def get_plan(self) -> dict:
        pass
