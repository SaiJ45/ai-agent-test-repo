from app.utils import calculate_total, format_user
import pytest

def test_calculate_total_normal_case():
    items = [{"price": 10, "quantity": 2}, {"price": 20, "quantity": 3}]
    assert calculate_total(items) == 80

def test_calculate_total_empty_list():
    items = []
    assert calculate_total(items) == 0

def test_calculate_total_none_input():
    items = None
    with pytest.raises(TypeError):
        calculate_total(items)

def test_calculate_total_non_numeric_input():
    items = [{"price": "ten", "quantity": 2}, {"price": 20, "quantity": 3}]
    with pytest.raises(TypeError):
        calculate_total(items)

def test_format_user_normal_case():
    name = "John"
    age = 30
    assert format_user(name, age) == f"Name: {name}, Age: {age}"

def test_format_user_none_input():
    name = None
    age = 30
    with pytest.raises(TypeError):
        format_user(name, age)

def test_format_user_non_numeric_age():
    name = "John"
    age = "thirty"
    with pytest.raises(TypeError):
        format_user(name, age)