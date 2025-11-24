"""
There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k.

        [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].

    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not.

    Constraint: You must write an algorithm with O(logN) runtime complexity.

Example:

    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0

    Output: 4
"""
# Atleast one half will always be sorted


def search(nums, target, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(search(nums, target, 0, len(nums) - 1))
