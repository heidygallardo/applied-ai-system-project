import json
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

class AIReviewer:
    def __init__(self):
        self.client = OpenAI()

    def review(self, summary: dict) -> dict:
        prompt = f"""
        You are an AI schedule review assistant for a pet care planning app.

        Your job is to review a generated daily schedule and suggest a better task order if needed.

        You will be given:
        - total available time
        - scheduled tasks
        - skipped tasks
        - critical skipped tasks

        Rules:
        1. Focus especially on high-priority skipped tasks.
        2. Only use task names that already exist in the provided tasks.
        3. Do not invent new tasks.
        4. Recommend a better ordering of tasks by name only.
        5. Keep recommendations practical and concise.
        6. If the current plan is already reasonable, you may keep the same order and respond with "schedule looks good".
        7. If a high-priority task was skipped, include it first in recommended_order.
        8. recommended_order should reflect the ideal priority order of tasks, even if some tasks did not fit in the current schedule.
        9. If a critical task was skipped, do not limit recommended_order to only the scheduled tasks.
        10. If any high-priority task is skipped, do NOT say "schedule looks good".
        11. Return your response in this exact Python dictionary-style structure:
        {{
            "assessment": "...",
            "critical_issues": ["..."],
            "recommended_order": ["..."],
            "recommendations": ["..."]
        }}

        Here is the schedule summary:
        {json.dumps(summary, indent=2)}
        """

        
        # call AI here
        response = self.client.chat.completions.create(
            model='gpt-5.4-mini',
            messages=[
                {
                    "role": "user",
                    "content": prompt
                },
                {
                    "role": "developer",
                    "content": "Return valid JSON only. Do not include markdown or extra text."
                },
            ]
        )

        content = response.choices[0].message.content

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            raise ValueError(f'Invalid JSON returned by AI: {content}')


