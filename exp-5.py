from abc import ABC, abstractmethod
from typing import Final


class BankAccount(ABC):

    def __init__(self, account_no: int, name: str, balance: float):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    @abstractmethod
    def calculate_interest(self) -> float:
        pass

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display(self) -> None:
        print("Account Number:", self.account_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):

    RATE: Final[float] = 0.04

    def calculate_interest(self) -> float:
        return self.balance * self.RATE


class CurrentAccount(BankAccount):

    RATE: Final[float] = 0.02

    def calculate_interest(self) -> float:
        return self.balance * self.RATE


account = SavingsAccount(101, "Bhargavi", 10000)

account.deposit(2000)
account.withdraw(1000)

account.display()

print("Interest:", account.calculate_interest())