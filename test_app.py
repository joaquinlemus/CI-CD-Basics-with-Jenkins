from app import add, sub

def test_addtion():
    assert add(2, 3) == 5

def test_subtraction():
    assert sub(5, 3) == 2
