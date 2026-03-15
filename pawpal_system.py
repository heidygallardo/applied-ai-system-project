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
        self.pets.append(pet)

    def edit_pet(self, pet_name: str, **updates) -> None:
        for pet in self.pets:
            if pet.name == pet_name:
                for key, value in updates.items():
                    setattr(pet, key, value)

    def remove_pet(self, pet_name: str) -> None:
        self.pets = [pet for pet in self.pets if pet.name != pet_name]

    def view_pets(self) -> list[Pet]:
        return self.pets

    def view_all_tasks(self) -> list[Task]:
        return [task for pet in self.pets for task in pet.get_tasks()]


class Scheduler:
    def __init__(self, tasks: Optional[list[Task]] = None, availability: Optional[list] = None):
        self.tasks: list[Task] = tasks or []
        self.availability: list = availability or []
        self.daily_plan: list[Task] = []
        self.explanation: str = ""

    def generate_plan(self) -> None:
        sorted_tasks = self.sort_tasks_by_priority()
        self.daily_plan = self.filter_tasks_by_time(sorted_tasks)
        self.explanation = self.build_explanation()

    def sort_tasks_by_priority(self) -> list[Task]:
        order = {"high": 0, "medium": 1, "low": 2}
        return sorted(self.tasks, key=lambda t: order.get(t.priority, 3))

    def filter_tasks_by_time(self, sorted_tasks: list[Task]) -> list[Task]:
        total_available = sum(self.availability)
        plan, time_used = [], 0
        for task in sorted_tasks:
            if not task.completed and time_used + task.duration <= total_available:
                plan.append(task)
                time_used += task.duration
        return plan

    def build_explanation(self) -> str:
        if not self.daily_plan:
            return "No tasks scheduled."
        
        total_available = sum(self.availability)
        total_used = sum(t.duration for t in self.daily_plan)
        skipped = [t for t in self.tasks if t not in self.daily_plan and not t.completed]

        lines = [f"- {t.name}: selected because it has {t.priority} priority ({t.duration} min)" for t in self.daily_plan]

        if skipped:
            skip_lines = [f"- {t.name}: skipped (not enough remaining time or lower priority)" for t in skipped]
            lines += ["\nSkipped:"] + skip_lines

        return (
            f"Plan uses {total_used} of {total_available} available minutes.\n"
            f"Tasks were sorted by priority (high → medium → low), then fit into available time:\n"
            + "\n".join(lines)
        )

    def get_plan(self) -> dict:
        return {"daily_plan": self.daily_plan, "explanation": self.explanation}
