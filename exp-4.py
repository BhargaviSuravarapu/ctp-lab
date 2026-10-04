import time
import tracemalloc


N = 1000000


def list_processing():
    return [x * x for x in range(N)]


def generator_processing():
    return (x * x for x in range(N))


# List
tracemalloc.start()

start = time.perf_counter()
data = list_processing()
list_time = time.perf_counter() - start

_, list_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()


# Generator
tracemalloc.start()

start = time.perf_counter()
data = generator_processing()

for _ in data:
    pass

generator_time = time.perf_counter() - start

_, generator_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()


print("List Processing")
print("Time:", list_time, "seconds")
print("Memory:", list_memory / 1024 / 1024, "MB")

print("\nGenerator Processing")
print("Time:", generator_time, "seconds")
print("Memory:", generator_memory / 1024 / 1024, "MB")