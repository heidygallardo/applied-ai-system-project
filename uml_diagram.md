classDiagram
    class Owner {
        +name: string
        +availability: list
        +preferences: dict
        +pets: list[Pet]
        +add_pet()
        +edit_pet()
        +remove_pet()
        +view_pets()
        +view_all_tasks() list[Task]
    }

    class Pet {
        +name: string
        +species: string
        +age: int
        +tasks: list[Task]
        +add_task(task: Task)
        +edit_task(task_name: str)
        +remove_task(task_name: str)
        +get_tasks() list[Task]
    }

    class Task {
        +name: string
        +duration: int
        +priority: string
        +category: string
        +frequency: string
        +completed: bool
        +time: string
        +update_priority()
        +update_duration()
        +update_frequency()
        +mark_complete()
        +get_task_info() dict
    }

    class Scheduler {
        +tasks: list[Task]
        +availability: list[int]
        +daily_plan: list[Task]
        +explanation: string
        +generate_plan()
        +sort_tasks_by_priority() list[Task]
        +sort_tasks_by_time() list[Task]
        +filter_tasks_by_time(sorted_tasks) list[Task]
        +filter_tasks_by_status(completed: bool) list[Task]
        +detect_conflicts() list[str]
        +build_explanation() str
        +get_plan() dict
        -_to_minutes(time_str) int
    }

    Owner "1" *-- "1..*" Pet : owns
    Pet "1" *-- "1..*" Task : owns
    Scheduler ..> Task : uses
