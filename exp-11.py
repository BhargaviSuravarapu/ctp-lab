from typing import List


def calculate_average(marks: List[float]) -> float:
    if not marks:
        raise ValueError("Marks list cannot be empty")

    return sum(marks) / len(marks)


def get_grade(average: float) -> str:
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def main() -> None:
    marks = list(map(float, input("Enter marks: ").split()))

    average = calculate_average(marks)
    grade = get_grade(average)

    print("Average:", average)
    print("Grade:", grade)


if __name__ == "__main__":
    main()