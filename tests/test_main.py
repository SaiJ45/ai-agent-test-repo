from app.main import divide, process_order

def test_divide():
    assert divide(10, 2) == 5


def test_process_order():
    items = [{"price": 10, "quantity": 2}]
    assert process_order(items) == 20