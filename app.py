import streamlit as st
from ai_reviewer import AIReviewer
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# ---------------------------------------------------------------------------
# Session state initialization
# ---------------------------------------------------------------------------
if "owner" not in st.session_state:
    st.session_state.owner = None
if "plan" not in st.session_state:
    st.session_state.plan = None

# ---------------------------------------------------------------------------
# Owner setup
# ---------------------------------------------------------------------------
st.subheader("Owner")
owner_name = st.text_input("Owner name", value="Heidy")
availability = st.number_input("Available time today (minutes)", min_value=10, max_value=480, value=90)

if st.button("Save Owner"):
    st.session_state.owner = Owner(name=owner_name, availability=[availability])
    st.success(f"Owner '{owner_name}' saved with {availability} min available.")

st.divider()

# ---------------------------------------------------------------------------
# Pet setup (only shown once owner exists)
# ---------------------------------------------------------------------------
if st.session_state.owner:
    st.subheader("Add a Pet")
    col1, col2 = st.columns(2)
    with col1:
        pet_name = st.text_input("Pet name")
    with col2:
        species = st.selectbox("Species", ["dog", "cat", "other"])

    if st.button("Add Pet"):
        if pet_name:
            pet = Pet(name=pet_name, species=species, age=0)
            st.session_state.owner.add_pet(pet)
            st.success(f"Pet '{pet_name}' added.")
        else:
            st.warning("Please enter a pet name.")

    # Show existing pets
    pets = st.session_state.owner.view_pets()
    if pets:
        st.write("**Your pets:**", ", ".join(p.name for p in pets))

    st.divider()

    # ---------------------------------------------------------------------------
    # Task setup (only shown once at least one pet exists)
    # ---------------------------------------------------------------------------
    if pets:
        st.subheader("Add a Task")
        pet_names = [p.name for p in pets]
        selected_pet_name = st.selectbox("Assign to pet", pet_names)

        col1, col2, col3 = st.columns(3)
        with col1:
            task_title = st.text_input("Task title")
        with col2:
            duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
        with col3:
            priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

        category = st.text_input("Category (e.g. grooming, exercise)", value="general")

        if st.button("Add Task"):
            if task_title:
                task = Task(name=task_title, duration=int(duration), priority=priority, category=category)
                selected_pet = next(p for p in pets if p.name == selected_pet_name)
                selected_pet.add_task(task)
                st.success(f"Task '{task_title}' added to {selected_pet_name}.")
            else:
                st.warning("Please enter a task title.")

        # Show all tasks grouped by pet
        all_tasks_exist = any(p.get_tasks() for p in pets)
        if all_tasks_exist:
            st.markdown("**Current tasks by pet:**")
            for pet in pets:
                if pet.get_tasks():
                    st.markdown(f"*{pet.name}*")
                    for t in pet.get_tasks():
                        st.write(f"  - {t.name} | {t.duration} min | {t.priority} priority")

        st.divider()

        # ---------------------------------------------------------------------------
        # Generate schedule
        # ---------------------------------------------------------------------------
        st.subheader("Generate Schedule")
        if st.button("Generate Schedule"):
            all_tasks = st.session_state.owner.view_all_tasks()
            if all_tasks:
                scheduler = Scheduler(tasks=all_tasks, availability=st.session_state.owner.availability)
                scheduler.generate_plan()

                plan = scheduler.get_plan()
                summary = scheduler.get_schedule_summary()
                reviewer = AIReviewer()
                ai_review = reviewer.review(summary)

                st.session_state.plan = plan
                st.session_state.ai_review = ai_review


            else:
                st.warning("Add at least one task before generating a schedule.")

        if st.session_state.plan:
            plan = st.session_state.plan
            st.markdown("### Today's Schedule")
            for i, task in enumerate(plan["daily_plan"], start=1):
                st.write(f"{i}. **{task.name}** — {task.duration} min [{task.priority.upper()}]")
            st.divider()
            st.markdown("**Why this plan:**")
            st.text(plan["explanation"])


            st.markdown("### AI REVIEW")
            st.markdown(f"Assessment: {ai_review['assessment']}")
            st.markdown("Critical Issues:")

            if ai_review["critical_issues"]:

                for issue in ai_review["critical_issues"]:
                    st.write(f"- {issue}")

            else:
                st.write("- None")

            st.markdown("**Recommended Order:**")
            for i, task_name in enumerate(ai_review["recommended_order"], start=1):
                st.write(f"{i}. {task_name}")

            st.markdown("**Recommendations:**")
            if ai_review["recommendations"]:
                for rec in ai_review["recommendations"]:
                    st.write(f"- {rec}")
            else:
                st.write("- None")

