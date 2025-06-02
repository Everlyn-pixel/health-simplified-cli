from models.entry import Entry
from models.user import User
from sqlalchemy.orm import Session
from datetime import date
import csv
import os
import uuid

def test_analytics_summary_and_export(test_db: Session, tmp_path):
    unique_email = f"analytics_{uuid.uuid4()}@example.com"
    user = User(name="Analytics User", email=unique_email)
    test_db.add(user)
    test_db.commit()
    test_db.refresh(user)
    entry1 = Entry(user_id=user.id, food="Apple", calories=95, date=date(2025, 6, 1))
    entry2 = Entry(user_id=user.id, food="Orange", calories=62, date=date(2025, 6, 2))
    test_db.add_all([entry1, entry2])
    test_db.commit()
    # Simulate analytics summary
    entries = test_db.query(Entry).filter(Entry.user_id == user.id).all()
    assert len(entries) == 2
    # Simulate export to CSV
    output_file = tmp_path / "analytics_test.csv"
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Date", "Food", "Calories", "User ID"])
        for entry in entries:
            writer.writerow([
                entry.id,
                entry.date,
                entry.food,
                entry.calories,
                entry.user_id
            ])
    # Check CSV content
    with open(output_file, "r") as f:
        lines = f.readlines()
    assert len(lines) == 3  # header + 2 entries
    assert "Apple" in lines[1] and "Orange" in lines[2]
