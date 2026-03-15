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
        +view_all_tasks()
    }

    class Pet {
        +name: string
        +species: string
        +age: int
        +tasks: list[Task]
        +add_task()
        +edit_task()
        +remove_task()
        +get_tasks()
    }

    class Task {
        +name: string
        +duration: int
        +priority: string
        +category: string
        +completed: bool
        +update_priority()
        +update_duration()
        +mark_complete()
        +get_task_info()
    }

    class Scheduler {
        +tasks: list[Task]
        +availability: list
        +daily_plan: list
        +explanation: string
        +generate_plan()
        +sort_tasks_by_priority()
        +filter_tasks_by_time()
        +build_explanation()
        +get_plan()
    }

    Owner --> Pet : owns (1..*)
    Pet --> Task : has (1..*)
    Scheduler --> Task : manages
    Scheduler --> Owner : uses availability
