# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

classes included:
1. Owner
    - Stores owner information (name, availability, preferences)
    - Manages pets (add, edit, remove, view)
    - Can view all pets and all tasks across pets

2. Pet 
    - Stores pet info (name, species, age)
    - manages tasks for that ped (add, edit, remove, view tasks)

3. Task
    - Respresents a single p;et care activity
    - stores task details (name, duration, priority, category, completion status)
    - allow updating task details or marking the task complete

4. Scheduler
    - Generates the daily care plan
    - Organizes tasks based on priority and available time
    - Filters tasks to fit constraints
    - Produces the schedule and explanation of the plan

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

    - Yes I changed the name of my class from tasks to task, task made more sense for my
        use case.
    - I added a frequency attribute to my Task class to keep track of how frequent task needs to be done. I was initially not tracking that.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
