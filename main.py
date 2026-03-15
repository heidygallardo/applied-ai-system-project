from pawpal_system import Task, Pet, Owner, Scheduler

# --- Create owner ---
owner = Owner(name="Heidy", availability=[90])  # 90 minutes available today

# --- Create pets with tasks ---
ares = Pet(name="Ares", species="Dog", age=3)
ares.add_task(Task(name="Morning Walk", duration=20, priority="high", category="exercise", frequency="daily"))
ares.add_task(Task(name="Bath", duration=30, priority="medium", category="grooming", frequency="weekly"))
ares.add_task(Task(name="Training", duration=15, priority="low", category="exercise", frequency="daily"))

mochi = Pet(name="Mochi", species="Cat", age=2)
mochi.add_task(Task(name="Litter Box", duration=10, priority="high", category="hygiene", frequency="daily"))
mochi.add_task(Task(name="Brushing", duration=15, priority="low", category="grooming", frequency="weekly"))
mochi.add_task(Task(name="Playtime", duration=20, priority="medium", category="exercise", frequency="daily"))

# --- Add pets to owner ---
owner.add_pet(ares)
owner.add_pet(mochi)

# --- Generate and print today's schedule ---
scheduler = Scheduler(tasks=owner.view_all_tasks(), availability=owner.availability)
scheduler.generate_plan()

# plan is a dict: {"daily_plan": [Task, ...], "explanation": str}
# plan["daily_plan"] — list of Task objects that fit in available time
# plan["explanation"] — string describing why each task was chosen or skipped
# each Task has: .name (str), .duration (int), .priority (str), .category (str), .frequency (str), .completed (bool)
plan = scheduler.get_plan()

total = sum(t.duration for t in plan["daily_plan"])
available = sum(owner.availability)

print("╔══════════════════════════════════════════════╗")
print("║         PAWPAL+  TODAY'S SCHEDULE            ║")
print(f"║         Owner: {owner.name:<8} | {available} min available   ║")
print("╚══════════════════════════════════════════════╝")

counter = 1
pet_tasks = {pet.name: [] for pet in owner.pets}
for task in plan["daily_plan"]:
    for pet in owner.pets:
        if task in pet.get_tasks():
            pet_tasks[pet.name].append(task)

for pet in owner.pets:
    if not pet_tasks[pet.name]:
        continue
    print(f"\n  {pet.name.upper()}")
    print("  " + "─" * 43)
    for task in pet_tasks[pet.name]:
        print(f"  {counter}. {task.name:<22} {task.duration:>3} min   [{task.priority.upper()}]")
        counter += 1

print("\n  " + "─" * 43)
print(f"  Total scheduled: {total} / {available} min")
print("\n  WHY THIS PLAN:")
print(plan["explanation"])
print("╚══════════════════════════════════════════════╝")
