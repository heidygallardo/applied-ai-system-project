from pawpal_system import Task, Pet, Owner, Scheduler
from ai_reviewer import AIReviewer
import logging 

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --- Create owner ---
owner = Owner(name="Heidy", availability=[90])  # 90 minutes available today

# --- Create pets with tasks (added out of order intentionally) ---
ares = Pet(name="Ares", species="Dog", age=3)
ares.add_task(Task(name="Training",    duration=15, priority="low",    category="exercise", frequency="daily",  time="14:00"))
ares.add_task(Task(name="Morning Walk",duration=20, priority="high",   category="exercise", frequency="daily",  time="07:00"))
ares.add_task(Task(name="Bath",        duration=30, priority="medium", category="grooming", frequency="weekly", time="11:30"))

mochi = Pet(name="Mochi", species="Cat", age=2)
mochi.add_task(Task(name="Playtime",   duration=20, priority="medium", category="exercise", frequency="daily",  time="15:00"))
mochi.add_task(Task(name="Litter Box", duration=10, priority="high",   category="hygiene",  frequency="daily",  time="07:10"))  # overlaps Morning Walk (07:00–07:20)
mochi.add_task(Task(name="Brushing",   duration=15, priority="low",    category="grooming", frequency="weekly", time="10:00"))

# Mark one task complete so filter_tasks_by_status has something to show
ares.tasks[0].mark_complete()  # Training is done

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

summary = scheduler.get_schedule_summary()
reviewer = AIReviewer()
ai_review = reviewer.review(summary)


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

print("\n╔══════════════════════════════════════════════╗")
print("║                 AI REVIEW                    ║")
print("╚══════════════════════════════════════════════╝")

print(f"\n  Assessment: {ai_review['assessment']}")

print("\n  Critical Issues:")
if ai_review["critical_issues"]:
    for issue in ai_review["critical_issues"]:
        print(f"  - {issue}")
else:
    print("  - None")

print("\n  Recommended Order:")
for i, task_name in enumerate(ai_review["recommended_order"], start=1):
    print(f"  {i}. {task_name}")

print("\n  Recommendations:")
if ai_review["recommendations"]:
    for rec in ai_review["recommendations"]:
        print(f"  - {rec}")
else:
    print("  - None")

# --- Demo: sort_tasks_by_time ---
print("\n╔══════════════════════════════════════════════╗")
print("║         SORTED BY TIME (earliest first)      ║")
print("╚══════════════════════════════════════════════╝")
for t in scheduler.sort_tasks_by_time():
    print(f"  {t.time}  {t.name:<22} {t.duration:>3} min  [{t.priority.upper()}]")

# --- Demo: filter_tasks_by_status ---
print("\n╔══════════════════════════════════════════════╗")
print("║         FILTER BY STATUS                     ║")
print("╚══════════════════════════════════════════════╝")
pending = scheduler.filter_tasks_by_status(completed=False)
done    = scheduler.filter_tasks_by_status(completed=True)

print(f"\n  Pending ({len(pending)}):")
for t in pending:
    print(f"  - {t.name}")

print(f"\n  Completed ({len(done)}):")
for t in done:
    print(f"  - {t.name}")

# --- Demo: detect_conflicts ---
print("\n╔══════════════════════════════════════════════╗")
print("║         CONFLICT DETECTION                   ║")
print("╚══════════════════════════════════════════════╝")
conflicts = scheduler.detect_conflicts()
if conflicts:
    for msg in conflicts:
        print(f"  {msg}")
else:
    print("  No conflicts found.")
