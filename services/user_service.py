from database.setup import SessionLocal
from models.user import User

def create_user(name: str, email: str):
    db = SessionLocal()
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    print(f"✅ User '{name}' with email '{email}' created.")
    db.close()

def list_users():
    db = SessionLocal()
    users = db.query(User).all()
    for user in users:
        print(f"{user.id}: {user.name} ({user.email})")
    db.close()