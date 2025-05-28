from models.user import User
from sqlalchemy.orm import Session

def test_user_placeholder():
    assert True

def test_create_user(test_db: Session):
    user = User(name="Test User", email="test@example.com")
    test_db.add(user)
    test_db.commit()
    test_db.refresh(user)
    assert user.id is not None
    assert user.name == "Test User"
