"""
Better version of selection sort.

* Time complexity: O(n*log(n))
"""
def heap_sort(array):
    def sift_down(array, n, index):
        def get_left_child_index(index):
            return 2*index+1
        def get_right_child_index(index):
            return 2*index+2

        largest = index
        left = get_left_child_index(index)
        right = get_right_child_index(index)
        if left < n and array[left] > array[largest]:
            largest = left
        if right < n and array[right] > array[largest]:
            largest = right

        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            sift_down(array, n, largest)

    def heapify(array):
        n = len(array)
        for i in range(n//2-1, -1, -1):
            sift_down(array, n, i)

    heapify(array)
    n = len(array)
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        sift_down(array, i, 0)

if __name__ == "__main__":
    print(f"--------------------------------Heap sort--------------------------------")
    n = 10000
    array = [
        random.randint(1, 100) for _ in range(n)
    ]
    start_time = time.time()
    heap_sort(array)
    end_time = time.time() - start_time
    print(f"Time heap sort: {end_time}")
    print(f"------------------------------------------------------------------------------")
