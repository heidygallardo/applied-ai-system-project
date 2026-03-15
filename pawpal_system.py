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
    completed: bool = False

    def update_priority(self, new_priority: str) -> None:
        pass

    def update_duration(self, new_duration: int) -> None:
        pass

    def mark_complete(self) -> None:
        pass

    def get_task_info(self) -> dict:
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def edit_task(self, task_name: str, **updates) -> None:
        pass

    def remove_task(self, task_name: str) -> None:
        pass

    def get_tasks(self) -> list[Task]:
        pass


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
