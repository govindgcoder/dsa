def search(nums, target):
    low = 0
    high = len(nums) - 1
    mid = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
    return low


# write and check to get this
# high ends up at the index of the largest element smaller than the target.
# low ends up at the index of the smallest element larger than tarrget.
arr = [1, 3, 5, 6]
print(search(arr, 2))
