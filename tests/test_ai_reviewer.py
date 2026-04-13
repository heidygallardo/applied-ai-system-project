import sys
from pathlib import Path

# Added parent directory to path so pawpal_system can be imported
sys.path.insert(0, str(Path(__file__).parent.parent))


from ai_reviewer import AIReviewer


def test_ai_reviewer_simple():

    """
    Verifies that result given by ai reviewer is a dictionary
    and that the expected keys are present such as assessment
    """
    reviewer = AIReviewer()

    summary = {
        "available_time": 30,
        "scheduled_tasks": [
            {
                "name": "Feed Cat",
                "duration": 15,
                "priority": "medium",
                "category": "care",
                "time": "09:00"
            }
        ],
        "skipped_tasks": [
            {
                "name": "Give Medication",
                "duration": 20,
                "priority": "high",
                "category": "health",
                "time": "08:00"
            }
        ],
        "critical_skipped_tasks": [
            {
                "name": "Give Medication #2",
                "duration": 20,
                "priority": "high",
                "category": "health",
                "time": "08:00"
            }
        ]
    }

    result = reviewer.review(summary)

    print('res',result)

    # simple check
    assert isinstance(result, dict)
    assert "assessment" in result
    assert "critical_issues" in result 
    assert "recommended_order" in result
    assert  "recommendations" in result
