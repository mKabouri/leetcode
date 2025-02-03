"""
Find the minimum and swap

* Time complexity: O(n**2)
"""
import time
import random

def selection_sort(array):
    size_arr = len(array)
    for i in range(size_arr):
        min_idx = i
        for j in range(i+1, size_arr):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

if __name__ == "__main__":
    print(f"--------------------------------Selection sort--------------------------------")
    n = 10000
    array = [
        random.randint(1, 100) for _ in range(n)
    ]
    start_time = time.time()
    selection_sort(array)
    end_time = time.time() - start_time
    print(f"Time selection sort: {end_time}")
    print(f"------------------------------------------------------------------------------")
