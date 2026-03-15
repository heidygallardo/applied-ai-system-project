from pawpal_system import Task, Pet

# Task Completion: Verify that calling mark_complete() actually changes the task's status.
def test_mark_complete_changes_status():
    task = Task(name="Bath", duration=30, priority="high", category="grooming")
    assert task.completed == False
    task.mark_complete()
    assert task.completed == True

# Task Addition: Verify that adding a task to a Pet increases that pet's task count.
def test_add_task_increases_count():
    pet = Pet(name="Ares", species="Dog", age=3)
    assert len(pet.get_tasks()) == 0
    pet.add_task(Task(name="Bath", duration=30, priority="high", category="grooming"))
    assert len(pet.get_tasks()) == 1