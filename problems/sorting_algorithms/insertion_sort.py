"""
Pick one element from the unsorted side and insert it in the sorted side

* Time complexity: O(n**2)
"""
import time
import random

def insertion_sort(array):
    size_arr = len(array)
    for i in range(1, size_arr):
        for j in range(i):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]

if __name__ == "__main__":
    print(f"--------------------------------Insertion sort--------------------------------")
    n = 10000
    array = [
        random.randint(1, 100) for _ in range(n)
    ]
    start_time = time.time()
    insertion_sort(array)
    end_time = time.time() - start_time
    print(f"Time insertion sort: {end_time}")
    print(f"------------------------------------------------------------------------------")
