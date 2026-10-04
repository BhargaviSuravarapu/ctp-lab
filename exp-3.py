from dataclasses import dataclass, field
from typing import Generic, TypeVar, List

T = TypeVar("T")


@dataclass
class Stack(Generic[T]):
    items: List[T] = field(default_factory=list)

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items.pop()

    def display(self) -> None:
        print("Stack:", self.items)


@dataclass
class Queue(Generic[T]):
    items: List[T] = field(default_factory=list)

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def display(self) -> None:
        print("Queue:", self.items)


stack = Stack[int]()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()
print("Popped:", stack.pop())
stack.display()


queue = Queue[int]()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()
print("Dequeued:", queue.dequeue())
queue.display()