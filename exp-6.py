from dataclasses import dataclass


# Traditional Class
class Student:
    def __init__(self, name: str, roll_no: int, marks: float):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks


# Dataclass
@dataclass
class StudentData:
    name: str
    roll_no: int
    marks: float


s1 = Student("Bhargavi", 101, 85.5)

s2 = StudentData("Bhargavi", 101, 85.5)

print("Traditional Class:")
print(s1.name, s1.roll_no, s1.marks)

print("\nDataclass:")
print(s2)