import heapq

nums = [1, 5, 2, 4, 11, 55]


def build_max_heap(nums):
    arr = [None] + nums
    heap_size = len(arr)

    def max_heapify(arr, heap_size, i):
        left = 2 * i
        right = 2 * i + 1
        largest = i
        if left < heap_size and arr[left] > arr[i]:
            largest = left
        if right < heap_size and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            max_heapify(arr, heap_size, largest)
        print(arr)

    for i in range(heap_size // 2, 0, -1):
        max_heapify(arr, heap_size, i)

    nums[:] = arr[1:]


# build_max_heap(nums)
heapq._heapify_max(nums)
heapq.heappop(nums)
print(nums)
