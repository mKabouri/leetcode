"""
Swap two adjacent elements if the first is larger than the second
so that the biggest will be the last one at the end of the iteration
and repeat the process.

* Time complexity: O(n**2)
"""
import time
import random

def bubble_sort(array):
    size_arr = len(array)
    for i in range(size_arr):
        for j in range(0, size_arr-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

if __name__ == "__main__":
    print(f"--------------------------------Bubble sort--------------------------------")
    n = 10000
    array = [
        random.randint(1, 100) for _ in range(n)
    ]
    start_time = time.time()
    bubble_sort(array)
    end_time = time.time() - start_time
    print(f"Time bubble sort: {end_time}")
    print(f"---------------------------------------------------------------------------")
