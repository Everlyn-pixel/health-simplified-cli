from models.entry import Entry
from sqlalchemy.orm import Session
from datetime import date

def test_entry_placeholder():
    assert "entry" != ""

def test_create_entry(test_db: Session):
    entry = Entry(user_id=1, food="Banana", calories=100, date=date(2025, 6, 1))
    test_db.add(entry)
    test_db.commit()
    test_db.refresh(entry)
    assert entry.id is not None
    assert entry.food == "Banana"
    assert entry.calories == 100
