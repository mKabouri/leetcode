"""
"divide and conquer algorithm which relies on a partition operation:
to partition an array, an element called a pivot is selected. All elements
smaller than the pivot are moved before it and all greater elements are
moved after it."

* Time complexity: O(n*log(n))
"""
import time
import random

def quick_sort(array, low, high):
    def partition(array, low, high):
        pivot = array[high]
        i = low
        for j in range(low, high):
            if array[j] <= pivot:
                array[j], array[i] = array[i], array[j]
                i += 1
        array[i], array[high] = array[high], array[i]
        return i

    if low < 0 or high <= low:
        return
    pivot = partition(array, low, high)
    quick_sort(array, low, pivot-1)
    quick_sort(array, pivot+1, high)

if __name__ == "__main__":
    print(f"--------------------------------Quick sort--------------------------------")
    n = 10000
    array = [
        random.randint(1, 100) for _ in range(n)
    ]
    start_time = time.time()
    quick_sort(array, 0, n-1)
    end_time = time.time() - start_time
    print(f"Time quick sort: {end_time}")
    print(f"------------------------------------------------------------------------------")
