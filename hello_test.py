from hello import greet

def test_greet():
    assert greet("Joshua") == "Hello, Sam!"


def test_empty():
    assert greet("") == "Hello, !"