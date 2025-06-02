from database.setup import SessionLocal
from models.user import User

def create_user(name: str):
    db = SessionLocal()
    user = User(name=name)
    db.add(user)
    db.commit()
    print(f"✅ User '{name}' created.")
    db.close()

def list_users():
    db = SessionLocal()
    users = db.query(User).all()
    for user in users:
        print(f"{user.id}: {user.name}")
    db.close()