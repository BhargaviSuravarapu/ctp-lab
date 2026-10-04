from queue import Queue
from threading import Thread
import time


queue = Queue(maxsize=5)


def producer() -> None:
    for i in range(1, 6):
        queue.put(i)
        print("Produced:", i)
        time.sleep(0.5)


def consumer() -> None:
    for i in range(1, 6):
        item = queue.get()
        print("Consumed:", item)
        queue.task_done()
        time.sleep(0.8)


producer_thread = Thread(target=producer)
consumer_thread = Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Producer-Consumer completed")