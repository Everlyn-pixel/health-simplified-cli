import pytest
from database.setup import get_db, Base, engine

@pytest.fixture(scope="function")
def test_db():
    # Create all tables before each test
    Base.metadata.create_all(bind=engine)
    db = next(get_db())
    yield db
    db.close()
    # Drop all tables after each test for isolation
    Base.metadata.drop_all(bind=engine)
