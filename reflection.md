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
    - Respresents a single pet care activity
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

    Yes I changed the name of my class from tasks to task, task made more sense for my use case.
    
    I added a frequency attribute to my Task class to keep track of how frequent task needs to be done. I was initially not tracking that.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?

My scheduler considers time, priority, and any conflicts there might be.

- How did you decide which constraints mattered most?

I decided what constraints mattered most based on app
requirements. For example, since I knew the app would generate a schedule, I knew time was one of the constraints that mattered most. 

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.

    My schedles sorts by priority by default not by scheduled time. 
- Why is that tradeoff reasonable for this scenario?
    It is reasonable since tasks that are marked with higher priority should be completed first.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

I used AI for brainstorming, debugging and refactoring.

- What kinds of prompts or questions were most helpful?

The prompts that were most helpful were the ones where I'd ask AI to explain why the error I was getting might occur and 
possible solutions.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

    One moment where I did not accept an AI suggestion as-is 
    was when it wanted for me to update my Owner class for a failing test which was uneccessary.

    I read through the suggestion and realized it was trying 
    to change the method rather than correctly testing it.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?

    I tested the following behaviors:
    - ensure sort tasks by time returns correct order
    - ensure only incomplete tasks are returned when filtering for pending
    - ensure tasks with overlapping time windows are flagged.
    - ensure calling mark_complete() actually changes the task's status
    - ensure adding a task to a Pet increases that pet's task count
- Why were these tests important?

    These tests were important because they check core logic the scheduler depends on to create a reliable daily schedule. 

**b. Confidence**

- How confident are you that your scheduler works correctly?

    My confidence is a 2/5 since I feel like I need to add more test cases to the app.

- What edge cases would you test next if you had more time?

    If I had more time I would test if when a task ends at 9pm and one start at the same time if it would count 
    as a conflict or not.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

    I am most satisfied with the UML diagram and documenting
    changes as needed.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

    I would improve on my test cases if I had another iteration.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

    I learned not to trust AI fully especially when it generates test cases.