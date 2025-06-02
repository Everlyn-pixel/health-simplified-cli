from database.setup import SessionLocal
from models.goal import Goal
from models.user import User

def set_goal(user_name, daily, weekly):
    db = SessionLocal()
    user = db.query(User).filter(User.name == user_name).first()
    if not user:
        print("User not found.")
        return
    goal = Goal(user_id=user.id, daily=daily, weekly=weekly)
    db.add(goal)
    db.commit()
    print("✅ Goal set.")
    db.close()

def list_goals(user_name):
    db = SessionLocal()
    user = db.query(User).filter(User.name == user_name).first()
    if not user:
        print("User not found.")
        return
    goals = db.query(Goal).filter(Goal.user_id == user.id).all()
    for goal in goals:
        print(f"Daily: {goal.daily}, Weekly: {goal.weekly}")
    db.close()
