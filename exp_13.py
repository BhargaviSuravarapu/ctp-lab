def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def main() -> None:
    celsius = float(input("Enter temperature in Celsius: "))

    fahrenheit = celsius_to_fahrenheit(celsius)

    print("Temperature in Fahrenheit:", fahrenheit)


if __name__ == "__main__":
    main()