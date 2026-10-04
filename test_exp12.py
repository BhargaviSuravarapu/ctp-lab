from exp_12 import calculate_total


def test_total():
    assert calculate_total([10, 20, 30]) == 60


def test_empty_list():
    assert calculate_total([]) == 0


def test_single_number():
    assert calculate_total([50]) == 50