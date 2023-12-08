from .utils import get_hand_type


def test_get_hand_type():
    assert get_hand_type("AAAAA") == 7
    assert get_hand_type("AA8AA") == 6
    assert get_hand_type("23332") == 5
    assert get_hand_type("TTT98") == 4
    assert get_hand_type("23432") == 3
    assert get_hand_type("A23A4") == 2
    assert get_hand_type("23456") == 1
