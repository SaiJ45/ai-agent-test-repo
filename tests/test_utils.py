from app.utils import format_user

def test_format_user():
    assert format_user("John", 25) == "Name: John, Age: 25"