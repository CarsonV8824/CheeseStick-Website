from src.database.database import Database
import pytest

#this file will test all databases

def test_get_data():
    db = Database(":memory:")  # Use in-memory database for testing
    db.add_data(("Cheddar", 10))
    db.add_data(("Mozzarella", 20))
    data = db.get_data()
    assert len(data) == 2
    assert data[0][1] == "Cheddar"
    assert data[0][2] == 10
    assert data[1][1] == "Mozzarella"
    assert data[1][2] == 20
    db.close()

def test_get_certain_data():
    db = Database(":memory:")
    db.add_data(("Gouda", 15))
    data = db.get_certain_data(1)
    assert data[1] == "Gouda"
    assert data[2] == 15
    db.close()

def test_add_data():
    db = Database(":memory:")
    db.add_data(("Brie", 5))
    data = db.get_data()
    assert len(data) == 1
    assert data[0][1] == "Brie"
    assert data[0][2] == 5
    db.close()