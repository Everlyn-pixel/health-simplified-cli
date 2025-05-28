from models.goal import Goal
from sqlalchemy.orm import Session

def test_goal_placeholder():
    assert 1 + 1 == 2

def test_create_goal(test_db: Session):
    goal = Goal(user_id=1, name="Test Goal")
    test_db.add(goal)
    test_db.commit()
    test_db.refresh(goal)
    assert goal.id is not None
    assert goal.name == "Test Goal"
