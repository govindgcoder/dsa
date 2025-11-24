def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
    return -1


# needs a sorted array okay?

arr = [1, 2, 5, 9, 22, 29, 33]
print(binary_search(arr, 22))
