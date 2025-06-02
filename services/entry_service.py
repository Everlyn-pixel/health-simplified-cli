from database.setup import SessionLocal
from models.entry import Entry
from models.user import User
from datetime import datetime

def add_entry(user_name, food, calories, date):
    db = SessionLocal()
    user = db.query(User).filter(User.name == user_name).first()
    if not user:
        print("User not found.")
        return
    # Convert date string to a Python date object
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d").date()
    entry = Entry(user_id=user.id, food=food, calories=calories, date=date)
    db.add(entry)
    db.commit()
    print(" Entry added.")
    db.close()

def list_entries(user_name=None, date=None):
    db = SessionLocal()
    query = db.query(Entry)
    if user_name:
        user = db.query(User).filter(User.name == user_name).first()
        if user:
            query = query.filter(Entry.user_id == user.id)
    if date:
        query = query.filter(Entry.date == date)
    for entry in query.all():
        print(f"{entry.id}: {entry.food} - {entry.calories} kcal on {entry.date}")
    db.close()

def update_entry(id, food=None, calories=None, date=None):
    db = SessionLocal()
    entry = db.query(Entry).get(id)
    if entry:
        if food:
            entry.food = food
        if calories:
            entry.calories = calories
        if date:
            entry.date = date
        db.commit()
        print(" Entry updated.")
    else:
        print("Entry not found.")
    db.close()

def delete_entry(id):
    db = SessionLocal()
    entry = db.query(Entry).get(id)
    if entry:
        db.delete(entry)
        db.commit()
        print(" Entry deleted.")
    else:
        print("Entry not found.")
    db.close()