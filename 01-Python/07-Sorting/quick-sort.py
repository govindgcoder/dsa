def partition(arr, low, high):
    key = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < key:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Above is the lomuto partition scheme gng


def quick_sort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)
        quick_sort(nums, low, pi - 1)
        quick_sort(nums, pi + 1, high)


arr = [1, 6, 2, 4, 3]
print("Before sorting:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("After sorting:", arr)
