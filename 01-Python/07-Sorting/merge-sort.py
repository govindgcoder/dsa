def merge(nums, low, mid, high):
    arr1 = nums[low : mid + 1]
    arr2 = nums[mid + 1 : high + 1]
    n1 = len(arr1)
    n2 = len(arr2)
    i, j, k = 0, 0, low
    # k is low since remember the nums starts at 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            nums[k] = arr1[i]
            i += 1
        else:
            nums[k] = arr2[j]
            j += 1
        k += 1
    while i < n1:
        nums[k] = arr1[i]
        i += 1
        k += 1
    while j < n2:
        nums[k] = arr2[j]
        j += 1
        k += 1


def merge_sort(nums, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(nums, low, mid)
        merge_sort(nums, mid + 1, high)
        merge(nums, low, mid, high)


arr = [1, 6, 2, 4, 3]
print("Before sorting:", arr)
merge_sort(arr, 0, len(arr) - 1)
print("After sorting:", arr)
