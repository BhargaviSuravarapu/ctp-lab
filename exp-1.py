import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = list(map(int, input("Enter elements: ").split()))

start = time.perf_counter()
sorted_arr = merge_sort(arr)
end = time.perf_counter()

print("Original Array:", arr)
print("Sorted Array:", sorted_arr)
print("Execution Time:", end - start, "seconds")
print("Time Complexity: O(n log n)")