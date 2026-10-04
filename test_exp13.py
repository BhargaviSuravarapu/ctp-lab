from exp_13 import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0


def test_conversion():
    celsius = 25
    fahrenheit = celsius_to_fahrenheit(celsius)

    assert round(fahrenheit_to_celsius(fahrenheit), 2) == 25