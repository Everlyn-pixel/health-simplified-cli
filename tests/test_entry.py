from models.entry import Entry
from sqlalchemy.orm import Session

def test_entry_placeholder():
    assert "entry" != ""

def test_create_entry(test_db: Session):
    entry = Entry(user_id=1, data="Test entry", date="2025-05-28")
    test_db.add(entry)
    test_db.commit()
    test_db.refresh(entry)
    assert entry.id is not None
